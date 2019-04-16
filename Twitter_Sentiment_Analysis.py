import tweepy
from textblob import TextBlob

# Twitter API Integration
consumer_key = 
consumer_secret = 

access_token = 
access_secret = 

# Tweepy Authorization Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create API variable
api = tweepy.API(auth)

# Create list of Public Tweets
public_tweets = api.search('Key Word Goes Here')

# Perform Sentiment Analysis
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    analysis_sentiment = analysis.sentiment
    print(analysis_sentiment)
