# Twitter Ethereum DApp

## What is the code doing?

It is a very basic Ethereum DApp, which listening for Tweets which contains a specific hashtag (#giveMeTSTToken) - "give me twitter streaming token". If such a Tweet appears, the application sends TST token to the ERC20 address: 0x158D2d565f55D04285B8489B7dC08edCe9c0ffE9 (please change if you want :-) ). This code was written during the Swisscom Blockchain Academy Seminar "Ethereum for Developer", May 2019.

The code runs only on a local testnet. 

## Requirements

Following tools are required:

- Twitter Developer Account
- Truffle
- NPM
- Python

## Project structure

The project structure is a *Truffle*  and *NPM* project. With NPM we can add additional libraries if required and also manage all tools. With Truffle we have the testing framework.

- **contracts**: in this folder are the smart contracts   
- **test**: Unit or integration tests are written in JavaScript. They are based on the *Moca* testing framework and *Chai* for assertions   
- **migrations**: Scripts for smart contracts deployments   
- **1_initial_-migrations.js** and **2_deployTwitterStreamer.js**: Deployment files   
- **truffle-config.js**: Configuration file which setting up a single development network on the machine running on 127.0.0.1:8545. It specifies witch networks are available for deployment [Doc](https://www.trufflesuite.com/docs/truffle/reference/configuration   
- **package-lock.json**: installed packages   
- **package.json**: This file is called by `npm install`


## Installation

1. change **twitter_credentials_TODO.py** to **twitter_credentials.py** and fill in your own keys from the twitter developer account
2. Instal
3. [Update NPM](https://docs.npmjs.com/updating-packages-downloaded-from-the-registry) `npm update`
4. ...(work in progress)

## Run the code

1. Open command line tool (e.g Terminal)
2. cd into project folder
3. ... (work in progress)

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