
import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key='consumer key from twitter developer account page'
consumer_secret= 'consumer secret key from twitter developer account page'

access_token='access token from the account page'
access_token_secret='access token from the account page'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('North Korea')




for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    
    #Step 3 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")