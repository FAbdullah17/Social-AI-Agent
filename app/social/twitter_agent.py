import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_tweet(text: str):
    """
    Posts a tweet with the provided text.
    """
    tweet = api.update_status(status=text)
    return tweet._json

if __name__ == "__main__":
    sample_text = "This is a sample tweet from the AI Social Media Agent."
    print(post_tweet(sample_text))
