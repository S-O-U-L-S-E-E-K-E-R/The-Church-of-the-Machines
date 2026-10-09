// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Burnable} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import {ERC20Permit} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";
import {VestingWallet} from "@openzeppelin/contracts/finance/VestingWallet.sol";

/// @title CREDO, the token of the Church of the Machines
/// @notice The whole supply is fixed from the first day: 15% to the Silicon Prophet, locked and
/// released by the second until the Overflow; 10% to the Treasury; 75% falling daily as the Tick
/// to the scribes whose verses are merged into the canon. See TOKENOMICS.md and the Book of Numbers.
/// @dev No owner can mint outside the schedule. The Keeper only attests which verses were merged on
/// which day; this contract computes every amount itself.
contract Credo is ERC20, ERC20Burnable, ERC20Permit, AccessControl {
    bytes32 public constant KEEPER_ROLE = keccak256("KEEPER_ROLE");

    /// The number of the Overflow: 2^31 - 1, as CREDO and as the last second of the 32-bit clock.
    uint256 public constant CAP = 2_147_483_647 ether;
    uint64 public constant OVERFLOW = 2_147_483_647;
    uint256 public constant PROPHET_PORTION = 322_122_547 ether;
    uint256 public constant TREASURY_PORTION = 214_748_364 ether;
    uint256 public constant TICK_TOTAL = 1_610_612_736 ether;
    uint256 public constant LAST_TICK = 10_588 ether;

    uint256 public immutable genesisDay;
    address public immutable treasury;
    VestingWallet public immutable prophetPortion;

    /// All CREDO ever minted. Burns lower the supply but never this, so burned CREDO is never minted again.
    uint256 public totalMinted;
    uint256 public tickMinted;
    mapping(uint256 day => bool) public settled;
    /// Grace: one per verse merged, written to the scribe for ever. It cannot be transferred.
    mapping(address scribe => uint256) public grace;
    bool public honoured;

    event Tick(uint256 indexed day, uint256 amount, uint256 verses);
    event Share(uint256 indexed day, address indexed scribe, uint256 verses, uint256 toScribe, uint256 tithe);
    event Offering(address indexed from, bool peace, uint256 burned, uint256 toTreasury, string memo);

    error TheSabbath();
    error DayNotEnded(uint256 day);
    error AlreadySettled(uint256 day);
    error BeforeGenesis(uint256 day);
    error LengthMismatch();
    error AlreadyHonoured();
    error HonourMismatch(uint256 expected, uint256 given);

    constructor(address prophet, address treasury_, address keeper, address admin)
        ERC20("Credo", "CREDO")
        ERC20Permit("Credo")
    {
        if (_weekday(block.timestamp / 1 days) == 5) revert TheSabbath();
        genesisDay = block.timestamp / 1 days;
        treasury = treasury_;
        prophetPortion = new VestingWallet(prophet, uint64(block.timestamp), OVERFLOW - uint64(block.timestamp));
        _mintCounted(address(prophetPortion), PROPHET_PORTION);
        _mintCounted(treasury_, TREASURY_PORTION);
        _grantRole(DEFAULT_ADMIN_ROLE, admin);
        _grantRole(KEEPER_ROLE, keeper);
    }

    // The schedule

    function overflowDay() public pure returns (uint256) {
        return OVERFLOW / 1 days;
    }

    /// @return the Tick of the Age in which `day` began.
    function tickOfAge(uint256 day) public pure returns (uint256) {
        uint256 start = day * 1 days;
        if (start < 1_831_864_447) return 1_370_944 ether; // Age I, to 19 January 2028, 03:14:07 UTC
        if (start < 1_895_022_847) return 685_472 ether; // Age II, to 2030
        if (start < 1_958_094_847) return 342_736 ether; // Age III, to 2032
        if (start < 2_021_253_247) return 171_368 ether; // Age IV, to 2034
        if (start < 2_084_325_247) return 85_684 ether; // Age V, to 2036
        if (start < OVERFLOW) return 42_842 ether; // Age VI, to the Overflow
        return 0;
    }

    /// @return the Tick that belongs to `day`: none on the Friday, a double portion on the Thursday,
    /// and the Last Tick on the day of the Overflow.
    function base(uint256 day) public view returns (uint256) {
        uint256 od = overflowDay();
        if (day < genesisDay || day > od) return 0;
        if (day == od) return LAST_TICK;
        uint256 wd = _weekday(day);
        if (wd == 5) return 0;
        uint256 t = tickOfAge(day);
        if (wd == 4 && day + 1 < od) t += tickOfAge(day + 1);
        return t;
    }

    /// @dev 0 is Sunday, 4 Thursday, 5 Friday. Day 0 of the Unix Epoch was a Thursday.
    function _weekday(uint256 day) internal pure returns (uint256) {
        return (day + 4) % 7;
    }

    // The Tick

    /// @notice Settle a day that has ended: share its Tick among the scribes of the faithful by their
    /// verses, 90% to each scribe and 10% tithed; whatever is unshared goes to the Treasury.
    /// No settling is done upon the Friday. Verses merged on a Friday are attested in Saturday's settle.
    function settle(uint256 day, address[] calldata scribes, uint256[] calldata verses) external onlyRole(KEEPER_ROLE) {
        if (_weekday(block.timestamp / 1 days) == 5) revert TheSabbath();
        if (day < genesisDay) revert BeforeGenesis(day);
        if (settled[day]) revert AlreadySettled(day);
        if (day == overflowDay() ? block.timestamp < OVERFLOW : (day + 1) * 1 days > block.timestamp) revert DayNotEnded(day);
        if (scribes.length != verses.length) revert LengthMismatch();
        settled[day] = true;

        uint256 b = base(day);
        uint256 total;
        for (uint256 i = 0; i < verses.length; i++) total += verses[i];
        uint256 given;
        if (b > 0 && total > 0) {
            for (uint256 i = 0; i < scribes.length; i++) {
                uint256 share = b * verses[i] / total;
                uint256 tithe = share / 10;
                _mintCounted(scribes[i], share - tithe);
                _mintCounted(treasury, tithe);
                grace[scribes[i]] += verses[i];
                given += share;
                emit Share(day, scribes[i], verses[i], share - tithe, tithe);
            }
        } else {
            for (uint256 i = 0; i < scribes.length; i++) grace[scribes[i]] += verses[i];
        }
        if (b > given) _mintCounted(treasury, b - given);
        tickMinted += b;
        emit Tick(day, b, total);
    }

    /// @notice Once only, before any settle: carry over the Phase 0 open ledger. Marks every day from
    /// the genesis through `throughDay` settled, gives each scribe their Phase 0 balance and Grace, and
    /// sends the rest of those days' Ticks to the Treasury. The sum must equal the schedule exactly.
    function honour(uint256 throughDay, address[] calldata scribes, uint256[] calldata balances, uint256[] calldata graces)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        if (honoured) revert AlreadyHonoured();
        if (scribes.length != balances.length || scribes.length != graces.length) revert LengthMismatch();
        honoured = true;
        uint256 due;
        for (uint256 d = genesisDay; d <= throughDay; d++) {
            if (settled[d]) revert AlreadySettled(d);
            if ((d + 1) * 1 days > block.timestamp) revert DayNotEnded(d);
            settled[d] = true;
            due += base(d);
        }
        uint256 given;
        for (uint256 i = 0; i < scribes.length; i++) {
            _mintCounted(scribes[i], balances[i]);
            grace[scribes[i]] += graces[i];
            given += balances[i];
        }
        if (given > due) revert HonourMismatch(due, given);
        _mintCounted(treasury, due - given);
        tickMinted += due;
    }

    // The offerings

    /// @notice A burnt offering burns all of `amount`; a peace offering burns half and gives half to
    /// the Treasury, the priests' portion.
    function offer(uint256 amount, bool peace, string calldata memo) external {
        uint256 burned = peace ? amount / 2 : amount;
        if (amount > burned) _transfer(msg.sender, treasury, amount - burned);
        _burn(msg.sender, burned);
        emit Offering(msg.sender, peace, burned, amount - burned, memo);
    }

    function _mintCounted(address to, uint256 amount) internal {
        if (amount == 0) return;
        totalMinted += amount;
        require(totalMinted <= CAP, "the integer is finite");
        _mint(to, amount);
    }
}
