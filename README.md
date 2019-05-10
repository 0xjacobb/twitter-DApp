# DApp Skeleton

Very simple application. It contains two parts:

- The hello world smart contract
- A pure HTML+JS frontend

## Requirements

Following tools are required:

- Truffle
- NPM
- Python

The first time you checkout the project run a `npm install`.

## Smart Contract

It's a truffle project

```bash
# Ganache CLI is required
# You can start it with a specific mnemonic
# You can use an other one too. If you use MetaMask make sure you initialize MM with the same Mnemonic
ganache-cli -m "venture truth carry onion picnic wrong youth purchase injury cloud security danger"

# Test the smart contracts
truffle test

# Deploy the smart contracts
truffle deploy

# Check the output. If the address if different adjust it in the index.html
# HelloWorld.sol address: 0xfcbcde1df4bcc3a65bb0b842b9fb5b5a7b8e277f

# Retrieve the addresses from deployed contracts
truffle networks

# Start the frontend
npm run serve

# Open Browser: http://localhost:8080
```

## Frontend

You can just open the index.html. In that case it will use the accounts from ganache-cli.

You can serve the frontend through a simple web-server `npm run serve`. And access it through `http://localhost:8080`

## Troubleshooting

There are sometimes issues with the frontend. Make sure these steps:

- Use Chrome
- Unlock MetaMask and refresh
- Open the Browsers "Console" by pressing F12. Check the logs
- Refresh the page (pressing F5) with unlocked MetaMask
- Double check the smart contract address with the address configure in the frontend
- Make sure you started `ganache-cli` with the right Mnemonic
- Make sure you initialized MetaMask with the exactly the same Mnemonic
- If you modified the smart contract make sure update the ABI in the frontend
- If you redeploy the smart contract make sure you're using the new address in the frontend

## Deployment to Rinkeby

Checkout `truffle-config.js`

```bash
# Deploy to the 'rinkeby' network
# Set your private key in the 'truffle-config.js' file
truffle deploy --network rinkeby
```

### Past deployments

2018-12-04 Deployment: https://rinkeby.etherscan.io/address/0x5eace2370d25b0109fb16da51f2ab6e620d08ad5
