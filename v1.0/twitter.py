import tweepy

class TwitterClient:
    
    def __init__(self, consumer_key, consumer_secret, bearer_token, access_token, access_token_secret) -> None:
        self.conKey = consumer_key
        self.conSec = consumer_secret
        self.bearToken = bearer_token
        self.accToken = access_token
        self.accTokenSec = access_token_secret
        self.CLIENT = tweepy.Client(self.bearToken, self.conKey, self.conSec, self.accToken, self.accTokenSec)
    
    def tweet(self, message):
        self.CLIENT.create_tweet(text=message)