import tweepy
import json
import os
from dotenv import load_dotenv

load_dotenv() 

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if not tweet.favorited:
            try:
                tweet.favorite()
                print("Tweet with id - " + str(tweet.id) + " has been liked")
            except Exception as e:
                print(e)

    def on_error(self, status):
        print(status)

def main(keywords):

    API_TOKEN = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_SECRET_TOKEN = os.getenv('ACCESS_SECRET_TOKEN')
    
    auth = tweepy.OAuthHandler(API_TOKEN, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["buyucoin" , "technology" , "python"])