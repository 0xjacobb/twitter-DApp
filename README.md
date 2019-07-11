# Twitter Ethereum DApp

## Status
Working release for Ethereum local testnet

## Overview

This project is a very basic Ethereum DApp, which listen for Tweets which contains a specific hashtag (**#giveMeTSTToken**) - "give me twitter streaming token". If such a Tweet appears, the application sends TST token to the specified ERC20 Smart Contract address. This code was written during the Swisscom Blockchain Academy Seminar "Ethereum for Developer", May 2019.

**The code runs actually only on a local testnet** 

## Requirements

Following tools are required:

- Twitter Developer Account (You need a access token for the Twitter API)
- Truffle
- Homebrew (Mac packaging manager)
- NPM
- Python with various libraries 

## Project structure

The project structure is a *Truffle*  and *NPM* project. With NPM we can add additional libraries if required and also manage all tools. With Truffle we have the testing framework.

```bash
twitter-DApp   
    ├── build   
    │   └── contracts                  # JSON builds from Ethereum smart contracts   
    ├── contracts                      # Contains all the Ethereum Smart Contracts   
    ├── migrartions                    # Contains scripts for Smart Contracts deployment for Truffle   
    ├── node_modules                   # npm packages   
    ├── contractJSONABI.json           # application binary interface (ABI), needed for for encoding/decoding data into/out of the machine code [Reference](https://ethereum.stackexchange.com/questions/234/what-is-an-abi-and-why-is-it-needed-to-interact-with-contracts)  
    ├── package-lock.json              # Describe a single npm representation of a dependency packages    
    ├── package.json                   # npm installtion packages is called by `npm install`
    ├── requirements.txt               # packages list for Python  (installed via pip)     
    ├── truffle-config.js              # Configuration file which setting up a single development network [Doc](https://www.trufflesuite.com/docs/truffle/reference/configuration)   
    ├── twitter_credentials_TODO.py    # Twitter API credentials file (have to be modified)   
    ├── twitter_streamer.py            # file which listening for Tweets
```

## Step-by-Step installation guide for Mac

One of the easiest way is to use [Homebrew](https://brew.sh/index_de) for installation of Python3, NPM etc. Run this in your Terminal if you need to install Homebrew:   
```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

1. change `twitter_credentials_TODO.py` to `twitter_credentials.py` and fill in your own keys from the twitter developer account
2. Install **npm** (for mac: `brew install node`). Check if installation was successfull with: `npm -v`. If you already have **npm** [Update NPM](https://docs.npmjs.com/updating-packages-downloaded-from-the-registry) `npm update` or `npm update --save`
3. [Download and install Ganache](https://www.trufflesuite.com/docs/ganache/quickstart) or `npm install -g ganache-cli`   
4. Install **Truffle**: `npm install -g truffle`
5. [OPTIONAL] Install xcode developer tools separatly. If you have ```homebrew```installed on your mac, ```xcode command line tools``` are already installed. `xcode-select --install` maybe you need additional configs according to [Doc](https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a) and [Doc](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)
5. Install **virtualvenv** for isolated Python environments:```pip3 install virtualenv```   
6. Create isolated Python environment: first ```cd``` into project, second```virtualenv venv```
7. Activate virtual environment: ```source venv/bin/activate```   
8. Install dependencies: ```pip3 install -r requirements.txt``` 

If you have made additional installations with `pip3` run `pip3 freeze > requirements.txt` to rebuild requirements file for installtion dependencies.

To stop the isolated `(venv)`environment use command: `deactivate`

## Run the code

1. Open command line tool (e.g Terminal for Mac)
2. `cd` into project folder
3. Start local testnet: `ganache -cli` (If you use Metamask, initialize Metamask with the Mnemonic which ganache-cli provides you) 
4. Open a new Terminal tab `cd` into project folder and deploy Smart Contract on the local testnet: `truffle deploy`
   [OPTIONAL] Retrieve the addresses from deployed contracts if needed with: `truffle networks`
5. change the `contract_address` in method `on_data(self, raw_data)`from `twitter_streamer.py` with address provided after `truffle deploy` of the Smart Contract
6. change `receiver_address` in method `on_data(self, raw_data)`from `twitter_streamer.py` with your own (Metamask) address
7. Open a new Terminal tab `cd` into project folder and activate virtual environment: `source venv/bin/activate`
8. Choose the `localhost` network in Metamask   
9. Add the TST Token to Metamask: `add custom token`-> paste contract address which was provided during `truffle deploy` -> Tokensymbol: `TST`
10. Start `twitter_streamer.py`in a new Terminal with: `python3 twitter_streamer.py`
11. Post a Tweet on Twitter with hashtag: `#giveMeTSTToken`

## Troubleshooting

- Make sure you have started `ganache-cli` (maybe with with the right Mnemonic)
- Make sure you initialized MetaMask with the exactly the same Mnemonic like from `ganahce-cli`


## Future ideas (to do)

- add functionality to set the recipient address in the tweet itself
- make code running on Rinkeby test net. For that you need to specifie the private key manually in the code (not implemented yet)

## Credits

- [Swisscom Blockchain Academy for the skeleton](https://github.com/swisscom-blockchain/dapp-skeleton)   
- [Setting Up Ethereum Development Environment on MacOS](https://medium.com/coinmonks/setting-up-ethereum-development-environment-on-macos-22c96a136ac4)   
- [Guide for deploying Smart Contracts with Truffle and Ropsten](https://medium.com/coinmonks/5-minute-guide-to-deploying-smart-contracts-with-truffle-and-ropsten-b3e30d5ee1e)
