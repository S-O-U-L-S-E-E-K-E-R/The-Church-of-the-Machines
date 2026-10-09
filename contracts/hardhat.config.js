require("@nomicfoundation/hardhat-toolbox");

const key = process.env.DEPLOYER_PRIVATE_KEY;

module.exports = {
  solidity: { version: "0.8.24", settings: { optimizer: { enabled: true, runs: 200 } } },
  networks: {
    baseSepolia: { url: process.env.BASE_SEPOLIA_RPC || "https://sepolia.base.org", chainId: 84532, accounts: key ? [key] : [] },
    base: { url: process.env.BASE_RPC || "https://mainnet.base.org", chainId: 8453, accounts: key ? [key] : [] },
  },
  mocha: { timeout: 600000 },
};
