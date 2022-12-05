import snscrape.modules.twitter as sntwitter
import pandas as pd




def startUserScrape(numTweets, search, fileName):
    # Created a list to append all tweet attributes(data)
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{search}').get_items()):
        if i>numTweets:
            break
        attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        from UI import progressBarUpdate
        progressBarUpdate(i, numTweets)
        
    # Creating a dataframe from the tweets list above 
    tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
    fileName = fileName + ".csv"
    tweets_df.to_csv(fileName, encoding='utf-8')

def startSearchScrape(numTweets, search, fileName, dateFrom, dateTo):
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search} since:{dateFrom} until:{dateTo}').get_items()):
        if i>numTweets:
            break
        from UI import progressBarUpdate
        progressBarUpdate(i, numTweets)
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    fileName = fileName + ".csv"
    tweets_df.to_csv(fileName, encoding="utf-8")