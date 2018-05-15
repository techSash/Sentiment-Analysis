import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from local_config import *
import json

class Streamer(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print("ERROR ", status)

if __name__ == "__main__":
    streamer = Streamer()
    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)

    stream = Stream(auth, streamer)
    stream.filter(track=["Narendra Modi", "Rahul Gandhi", "BJP", "INC"])
