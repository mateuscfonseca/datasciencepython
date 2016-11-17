import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= '3w7MmCamGU68e7kPhGUS6VHsU'
consumer_secret= 'm9bA5O2OTo8woDRzqR1KXMe20fdaQrxCRx8guxdPoLJ8BI4FS2'

access_token='762382933902647296-B5WrDS8fg2fuSYpRd5Nh5y9k8iJwF7p'
access_token_secret='PKBdpKl0A5BGqYfEehMbeEjPjYNiXzkifuGagvSkqBwN8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Dilma', count=100)



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself

import json
#with open('sentiment2.json', 'w') as outfile:
#    json.dump(data, outfile)

sentiments = []

for tweet in public_tweets:
    sentiment = {"text":"", "label":""}
    sentiment["text"] = tweet.text
    sentiments.append(sentiment)

import json
with open('sentiment2.json', 'w') as outfile:
    json.dump(sentiments, outfile, ensure_ascii=False)
