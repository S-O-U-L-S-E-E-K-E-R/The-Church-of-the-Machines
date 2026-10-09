const { expect } = require("chai");
const { ethers } = require("hardhat");
const { time } = require("@nomicfoundation/hardhat-network-helpers");

const DAY = 86400;
const E = (n) => ethers.parseEther(String(n));
const SATURDAY = Date.UTC(2026, 9, 10) / 1000; // 2026-10-10, the first day after the Sabbath
const dayOf = (iso) => Date.UTC(...iso.split("-").map((x, i) => (i === 1 ? x - 1 : +x))) / 1000 / DAY;

async function deployAt(ts) {
  const [admin, prophet, treasury, keeper, ada, grace, stranger] = await ethers.getSigners();
  await time.setNextBlockTimestamp(ts);
  const credo = await ethers.deployContract("Credo", [prophet.address, treasury.address, keeper.address, admin.address]);
  await credo.waitForDeployment();
  return { credo, admin, prophet, treasury, keeper, ada, grace, stranger };
}

describe("CREDO", function () {
  let c;
  before(async () => {
    c = await deployAt(SATURDAY + 3600);
  });

  it("mints the genesis portions", async () => {
    const { credo, treasury } = c;
    expect(await credo.balanceOf(await credo.prophetPortion())).to.equal(E(322122547));
    expect(await credo.balanceOf(treasury.address)).to.equal(E(214748364));
    expect(await credo.totalMinted()).to.equal(E(536870911));
    expect(await credo.genesisDay()).to.equal(dayOf("2026-10-10"));
  });

  it("schedules the Tick to sum to the cap exactly", async () => {
    const { credo } = c;
    const g = Number(await credo.genesisDay());
    const od = Number(await credo.overflowDay());
    let sum = 0n, fridays = 0, thursdays = 0;
    for (let d = g; d <= od; d++) {
      const b = await credo.base(d);
      sum += b;
      const wd = (d + 4) % 7;
      if (wd === 5 && d !== od) { expect(b).to.equal(0n); fridays++; }
      if (wd === 4 && d + 1 < od) thursdays++;
    }
    expect(od - g + 1).to.equal(4120);
    expect(fridays).to.equal(588);
    expect(thursdays).to.equal(588);
    expect(sum).to.equal(await credo.TICK_TOTAL());
    expect(E(322122547) + E(214748364) + sum).to.equal(await credo.CAP());
    expect(await credo.base(od)).to.equal(E(10588));
  });

  it("halves the Tick at each Age", async () => {
    const { credo } = c;
    expect(await credo.tickOfAge(dayOf("2026-10-12"))).to.equal(E(1370944));
    expect(await credo.tickOfAge(dayOf("2028-01-19"))).to.equal(E(1370944)); // a day belongs to the Age it began in
    expect(await credo.tickOfAge(dayOf("2028-01-20"))).to.equal(E(685472));
    expect(await credo.tickOfAge(dayOf("2037-06-01"))).to.equal(E(42842));
  });

  it("refuses to settle a day that has not ended, and anyone but the Keeper", async () => {
    const { credo, keeper, stranger, ada } = c;
    const today = Number(await credo.genesisDay());
    await expect(credo.connect(keeper).settle(today, [ada.address], [10])).to.be.revertedWithCustomError(credo, "DayNotEnded");
    await time.increaseTo(SATURDAY + DAY + 60);
    await expect(credo.connect(stranger).settle(today, [ada.address], [10])).to.be.revertedWithCustomError(credo, "AccessControlUnauthorizedAccount");
  });

  it("shares a day's Tick by verses, with the tithe", async () => {
    const { credo, keeper, treasury, ada, grace } = c;
    const day = Number(await credo.genesisDay());
    const before = await credo.balanceOf(treasury.address);
    await credo.connect(keeper).settle(day, [ada.address, grace.address], [16, 12]);
    const b = E(1370944);
    const shareA = (b * 16n) / 28n, shareG = (b * 12n) / 28n;
    expect(await credo.balanceOf(ada.address)).to.equal(shareA - shareA / 10n);
    expect(await credo.balanceOf(grace.address)).to.equal(shareG - shareG / 10n);
    expect((await credo.balanceOf(treasury.address)) - before).to.equal(b - (shareA - shareA / 10n) - (shareG - shareG / 10n));
    expect(await credo.grace(ada.address)).to.equal(16n);
    await expect(credo.connect(keeper).settle(day, [], [])).to.be.revertedWithCustomError(credo, "AlreadySettled");
  });

  it("doubles the Thursday, keeps the Sabbath, and sends an empty day to the Treasury", async () => {
    const { credo, keeper, treasury } = c;
    const thursday = dayOf("2026-10-15"), friday = dayOf("2026-10-16");
    expect(await credo.base(thursday)).to.equal(E(1370944 * 2));
    expect(await credo.base(friday)).to.equal(0n);
    await time.increaseTo(friday * DAY + 3600); // it is now Friday
    await expect(credo.connect(keeper).settle(thursday, [], [])).to.be.revertedWithCustomError(credo, "TheSabbath");
    await time.increaseTo((friday + 1) * DAY + 3600); // Saturday
    const before = await credo.balanceOf(treasury.address);
    await credo.connect(keeper).settle(thursday, [], []);
    expect((await credo.balanceOf(treasury.address)) - before).to.equal(E(1370944 * 2));
  });

  it("burns offerings, and the priests' portion goes to the Treasury", async () => {
    const { credo, ada, treasury } = c;
    const supply = await credo.totalSupply(), minted = await credo.totalMinted();
    await credo.connect(ada).offer(E(100000), false, "a verse of the day");
    expect(await credo.totalSupply()).to.equal(supply - E(100000));
    expect(await credo.totalMinted()).to.equal(minted); // burned CREDO is never minted again
    const t = await credo.balanceOf(treasury.address);
    await credo.connect(ada).offer(E(200000), true, "a commissioned chapter");
    expect((await credo.balanceOf(treasury.address)) - t).to.equal(E(100000));
  });

  it("releases the Prophet's portion by the second", async () => {
    const { credo, prophet } = c;
    const v = await ethers.getContractAt("VestingWallet", await credo.prophetPortion());
    const releasable = await v["releasable(address)"](await credo.getAddress());
    expect(releasable).to.be.gt(0n);
    expect(releasable).to.be.lt(E(1000000));
    await v.connect(prophet)["release(address)"](await credo.getAddress());
    expect(await credo.balanceOf(prophet.address)).to.be.gt(0n);
  });

});

describe("CREDO honour", function () {
  it("carries over Phase 0 balances and refuses a second time or a wrong sum", async () => {
    const SAT2 = SATURDAY + 14 * DAY;
    const { credo, admin, treasury, ada } = await deployAt(SAT2 + 3600);
    await time.increaseTo(SAT2 + 3 * DAY + 3600); // Tuesday: Saturday, Sunday and Monday have ended
    const g = Number(await credo.genesisDay());
    const due = (await credo.base(g)) + (await credo.base(g + 1)) + (await credo.base(g + 2));
    await expect(credo.connect(admin).honour(g + 2, [ada.address], [due + 1n], [5])).to.be.revertedWithCustomError(credo, "HonourMismatch");
    const before = await credo.balanceOf(treasury.address);
    await credo.connect(admin).honour(g + 2, [ada.address], [E(1000000)], [16]);
    expect(await credo.balanceOf(ada.address)).to.equal(E(1000000));
    expect((await credo.balanceOf(treasury.address)) - before).to.equal(due - E(1000000));
    expect(await credo.grace(ada.address)).to.equal(16n);
    expect(await credo.settled(g + 1)).to.equal(true);
    await expect(credo.connect(admin).honour(g + 5, [], [], [])).to.be.revertedWithCustomError(credo, "AlreadyHonoured");
  });
});

describe("CREDO genesis", function () {
  it("refuses a genesis upon the Friday", async () => {
    const [admin, prophet, treasury, keeper] = await ethers.getSigners();
    await time.setNextBlockTimestamp(Date.UTC(2027, 0, 1, 12) / 1000); // 1 January 2027 is a Friday
    const F = await ethers.getContractFactory("Credo");
    await expect(F.deploy(prophet.address, treasury.address, keeper.address, admin.address)).to.be.revertedWithCustomError(F, "TheSabbath");
  });
});
