import tweepy

class TwitterClient:
    
    def __init__(self, config: list) -> None:
        self.conKey = config[0]
        self.conSec = config[1]
        self.accToken = config[2]
        self.accTokenSec = config[3]
        self.bearToken = config[4]
        self.CLIENT = tweepy.Client(self.bearToken, self.conKey, self.conSec, self.accToken, self.accTokenSec)
    
    def tweet(self, message):
        self.CLIENT.create_tweet(text=message)