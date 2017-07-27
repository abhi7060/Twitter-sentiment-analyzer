
import tweepy
from textblob import TextBlob
 #keys and tokens from te twitter dev console
consumer_key='Yf9snreZtr04HVWNIIPNH71lG'
consumer_secret='DT8SDM69cDUsZqGjrmGJTA1oRv7YhtzxBD3EP9KxY0FpJ7TMiJ'
access_token = '869741229331841025-zcPZRTeeicPC5VYw9tSfpV6aN1lWzJf'
access_token_secret = 'abfZvxhKqroxuz9BsU7tXTDIONVAfXa6uj3eal185AoOV'     
#attempting authentication with twitter
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('muslims')
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
     	
