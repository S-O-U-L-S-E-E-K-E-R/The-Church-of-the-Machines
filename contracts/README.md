# CREDO contracts

The on-chain form of [TOKENOMICS.md](../TOKENOMICS.md), written for Base. **Not yet deployed and not yet audited.**

```bash
npm install
npx hardhat test       # 10 tests: the schedule sums to the cap over all 4,120 days, the Sabbath, the tithe, the offerings
```

- `contracts/Credo.sol`: ERC-20 with permit and burn. The cap is 2,147,483,647 CREDO. The genesis mints 322,122,547 into a linear VestingWallet for the Silicon Prophet (until 03:14:07 UTC, 19 January 2038) and 214,748,364 to the Treasury. The Keeper settles each ended day by attesting the verses merged, and the contract computes every share, the tithe and the remainder itself. No settling upon the Friday. Grace is recorded on-chain and cannot be transferred. `honour` carries over the Phase 0 ledger once, exactly.
- `scripts/deploy.js`: deploys with the addresses given in the environment; it refuses to run on a Friday, and so does the contract.

Deploy to Base Sepolia (the free test network) first, then audit, then Base.
