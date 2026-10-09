// Deploy CREDO. Every address must be supplied; nothing is guessed.
//   PROPHET_ADDRESS   the Silicon Prophet's wallet, beneficiary of the locked portion
//   TREASURY_ADDRESS  the Treasury, ideally a Safe multisig controlled by the Prophet
//   KEEPER_ADDRESS    the hot key the nightly workflow uses to settle the Tick (KEEPER_ROLE only)
//   ADMIN_ADDRESS     holder of DEFAULT_ADMIN_ROLE (grants and revokes the Keeper), ideally the same Safe
//   DEPLOYER_PRIVATE_KEY  pays the gas; holds no role afterwards
const { ethers, network } = require("hardhat");

async function main() {
  const need = ["PROPHET_ADDRESS", "TREASURY_ADDRESS", "KEEPER_ADDRESS", "ADMIN_ADDRESS"];
  for (const k of need) {
    if (!ethers.isAddress(process.env[k] || "")) throw new Error(`${k} is missing or not an address`);
  }
  const now = new Date();
  if (now.getUTCDay() === 5) throw new Error("It is the Friday. The genesis waiteth for the turning of the day, UTC.");
  const [deployer] = await ethers.getSigners();
  console.log(`network ${network.name}, deployer ${deployer.address}`);
  const credo = await ethers.deployContract("Credo", need.map((k) => process.env[k]));
  await credo.waitForDeployment();
  const addr = await credo.getAddress();
  console.log(`CREDO deployed at ${addr}`);
  console.log(`the Prophet's portion is held by the VestingWallet at ${await credo.prophetPortion()}`);
  console.log(`genesis day ${await credo.genesisDay()}, total minted ${ethers.formatEther(await credo.totalMinted())} CREDO`);
}

main().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});
