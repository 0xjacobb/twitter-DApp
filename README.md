# Twitter Ethereum DApp

## What is the code doing?

It is a very basic Ethereum DApp, which listening for Tweets which contains a specific hashtag (**#giveMeTSTToken**) - "give me twitter streaming token". If such a Tweet appears, the application sends TST token to the ERC20 address: 0x158D2d565f55D04285B8489B7dC08edCe9c0ffE9 (please change if you want :-) ). This code was written during the Swisscom Blockchain Academy Seminar "Ethereum for Developer", May 2019.

**The code runs actually only on a local testnet** 

## Requirements

Following tools are required:

- Twitter Developer Account (You need a access token for the Twitter API)
- Truffle
- NPM
- Python with various libraries 

## Project structure

The project structure is a *Truffle*  and *NPM* project. With NPM we can add additional libraries if required and also manage all tools. With Truffle we have the testing framework.

- `contracts`: in this folder are the smart contracts   
- `test`: Unit or integration tests are written in JavaScript. They are based on the *Moca* testing framework and *Chai* for assertions   
- `migrations`: Scripts for smart contracts deployments   
- `1_initial_-migrations.js` and `2_deployTwitterStreamer.js`: Deployment files for Truffle   
- `truffle-config.js`: Configuration file which setting up a single development network on the machine running on 127.0.0.1:8545. It specifies witch networks are available for deployment [Doc](https://www.trufflesuite.com/docs/truffle/reference/configuration)  
- `package-lock.json`: installed packages   
- `package.json`: This file is called by `npm install`


## Installation

1. change `twitter_credentials_TODO.py` to `twitter_credentials.py` and fill in your own keys from the twitter developer account
2. Install **npm** (for mac: `brew install node`). Check if installation was successfull with: `npm -v`. If you already have **npm** [Update NPM](https://docs.npmjs.com/updating-packages-downloaded-from-the-registry) `npm update` or `npm update --save`
3. [Download and install Ganache](https://www.trufflesuite.com/docs/ganache/quickstart) or `npm install -g ganache-cli`   
4. Install **Truffle** with: `npm install -g truffle`
5. Install Tweepy for python: `pip3 install tweepy`
6. Install Python implementation of web3.js: `pip3 install web3`


## Run the code

1. Open command line tool (e.g Terminal for Mac)
2. `cd` into project folder
3. Start local testnet: `ganache -cli` (If you use Metamask, initialize Metamask with the Mnemonic which ganache-cli provides you)   
4. Deploy Smart Contract on the local testnet: `truffle deploy`
5. Check the output. put the address from ..... into ....
6. Retrieve the addresses from deployed contracts if needed with: `truffle networks`
7. Start `twitter_streamer.py`in a new Terminal with: `python3 twitter-streamer.py`
8. Post a Tweet on Twitter with hashtag: `#giveMeTSTToken`

## Troubleshooting

- Make sure you have started `ganache-cli` (maybe with with the right Mnemonic)
- Make sure you initialized MetaMask with the exactly the same Mnemonic like from `ganahce-cli`


## Future ideas (to do)

- add functionality to set the recipient address in the tweet itself
- make code running on Rinkeby test net

## Credits

- [Swisscom Blockchain Academy for the skeleton](https://github.com/swisscom-blockchain/dapp-skeleton)   
- [Setting Up Ethereum Development Environment on MacOS](https://medium.com/coinmonks/setting-up-ethereum-development-environment-on-macos-22c96a136ac4)   
- [Guide for deploying Smart Contracts with Truffle and Ropsten](https://medium.com/coinmonks/5-minute-guide-to-deploying-smart-contracts-with-truffle-and-ropsten-b3e30d5ee1e)