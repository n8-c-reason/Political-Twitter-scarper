# import tweepy
# import time


# consumer_key = "iHp8Z6O5mWxsqEJSr9KPgC6Uo" #Your API/Consumer key 
# consumer_secret = "2eelFSj9y2Ty5froBMXeKT0YLy8J3oCZCw31tuGuiyaqmyrGB1" #Your API/Consumer Secret Key
# access_token = "1572217882183860224-LmMIvqrDKiEYZ8tFiCWQM8QqOP9J4o"    #Your Access token key
# access_token_secret = "6L8T37mMuXFSRYOkmiZNXSOF0rSeTjAFQzqnWdlGe68GF" #Your Access token Secret key


# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret,
#     access_token, access_token_secret
# )


# #Instantiate the tweepy API
# api = tweepy.API(auth, wait_on_rate_limit=True)


# username = "ryanair"
# no_of_tweets =5


# try:
#     #The number of tweets we want to retrieved from the user
#     tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
#     #Pulling Some attributes from the tweet
#     attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

#     #Creation of column list to rename the columns in the dataframe
#     columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
#     #Creation of Dataframe
#     tweets_df = pd.DataFrame(attributes_container, columns=columns)
# except BaseException as e:
#     print('Status Failed On,',str(e))
#     time.sleep(3)

import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:HenryMullen500').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])

tweets_df.to_csv('test2.csv', encoding='utf-8')