# Twitter Ethereum DApp

## What is the code doing?

It is a very basic Ethereum DApp, which listening for Tweets which contains a specific hashtag (#giveMeTSTToken) - "give me twitter streaming token". If such a Tweet appears, the application sends TST token to the ERC20 address: 0x158D2d565f55D04285B8489B7dC08edCe9c0ffE9 (please change if you want :-) ). This code was written during the Swisscom Blockchain Academy Seminar "Ethereum for Developer", May 2019.

The code runs only on a local testnet. 

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

# Check the output. If the address is different adjust it in the index.html
# HelloWorld.sol address: 0xfcbcde1df4bcc3a65bb0b842b9fb5b5a7b8e277f

# Retrieve the addresses from deployed contracts
truffle networks

# Start the frontend
npm run serve

# Open Browser: http://localhost:8080
```

## Troubleshooting

- Make sure you started `ganache-cli` with the right Mnemonic
- Make sure you initialized MetaMask with the exactly the same Mnemonic


## Future ideas (to do)

- add functionality to set the recipient address in the tweet itself
- make code running on Rinkeby test net

## Credits

- [Swisscom Blockchain Academy for the skeleton](https://github.com/swisscom-blockchain/dapp-skeleton)   
- 