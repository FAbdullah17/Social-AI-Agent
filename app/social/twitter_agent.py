import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

def post_tweet(text):
    """
    Posts a tweet with the given text.
    """
    try:
        tweet = api.update_status(status=text)
        return f"Tweet posted successfully: {tweet.id}"
    except tweepy.TweepyException as e:
        return f"Failed to post tweet: {e}"

# Example usage
if __name__ == "__main__":
    sample_text = "Hello, this is a test tweet from my AI social media agent!"
    print(post_tweet(sample_text))
