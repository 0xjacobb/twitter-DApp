from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re

import twitter_credentials
from web3 import Web3, HTTPProvider

'''
TWITTER AUTHENTICATOR
Handels connection to Twitter API
'''


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        # Authenticate code
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        # Authenticate application
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


'''
TWITTER STREAMER
Class for streaming and processing tweets
'''


class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    '''
    This method handles Twitter authentication and the connection to the twitter Streaming API
    Save tweets to file 'fetched_tweets_filename'
    '''

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # Create object
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()

        # create a data stream
        stream = Stream(auth, listener)

        # Define words for filtering Twitter streams
        stream.filter(track=hash_tag_list)


'''
TWITTER STREAM LISTENER
Class that inherit from StreamListener
Prints received tweets to stdout
'''


class TwitterListener(StreamListener):

    # Constructor
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.i = 0
        print("--------- START TWITTER LISTENER -----------\n")

    # Method who takes the data (listening to tweets) and interact with Smart Contract
    def on_data(self, raw_data):
         # TwitterStreamer.sol Smart Contract address which was provided during `truffle deploy`
        contract_address = '0x76753Bbb25FB8B0ADe41111b349A9F88FcF61c86'

        # Address which receives the TST Tokken
        receiver_address = '0x6ac0265dEB25f89Ab2074AACd8741F850fB74119'

        try:
            json_load = json.loads(raw_data)
            text = json_load['text']
            coded = text.encode('utf-8')
            s = str(coded)
            print("########## NEW TWEET: Nr: %i ########## \n" %
                  (self.i), s[2:-1])

            self.i += 1
            #print("Address is: ", re.search("0x.{40}",s).group())
            #receiver_address = re.search("0x.{40}",s).group()

            with open("./contractJSONABI.json") as f:
                info_json = json.load(f)
            abi = info_json
            w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
            free_tokkens_instance = w3.eth.contract(
                address=contract_address, abi=abi,)

            '''
            set sender account (Account from ganache). 
            Account [0] is the private key of the Smart Contract owner. Truffle deploy uses ganache-cli
            ganache-cli has the private key implmented in the node. Default key: [0]
            '''
            w3.eth.defaultAccount = w3.eth.accounts[0]

            '''send message to contract. If it is not working with recevier_address try
            tx_hash = free_tokkens_instance.functions.mintToken('0x9b26a3C40d32BD9e40266711Fd89ea9387340E90').transact()
            '''
            print('Get some Tokens...')
            tx_hash = free_tokkens_instance.functions.mintToken(
                receiver_address).transact()

            # Wait for transaction to be mined...
            w3.eth.waitForTransactionReceipt(tx_hash)

            '''
            Read out the balance of the recipient
            If it is not working with recevier_address try
            print('Balance: {}'.format(free_tokkens_instance.functions.balanceOf('0x9b26a3C40d32BD9e40266711Fd89ea9387340E90').call()))
            '''
            print('Balance: {}'.format(
                free_tokkens_instance.functions.balanceOf(receiver_address).call()))

            # Save tweets to file for analysis if needed
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(raw_data)
            return True

        except BaseException as e:
            print("Error on raw_data: %s" % str(e))
        return True

    # Method who handles Twitter API errors
    def on_error(self, status_code):
        '''
        402 error from twitter API = hit the rate limit. You have to wait
        a certain time before proceed otherwise Twitter looks the app out
        '''
        if status_code == 420:
            return False
        print(status_code)


if __name__ == "__main__":
    hash_tag_list = ["giveMeTSTToken"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
