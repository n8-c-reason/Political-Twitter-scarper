import snscrape.modules.twitter as sntwitter
import pandas as pd




def startScrape(numTweets, search, fileName):
    # Created a list to append all tweet attributes(data)
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{search}').get_items()):
        if i>numTweets:
            break
        attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe from the tweets list above 
    tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
    fileName = fileName + ".csv"
    tweets_df.to_csv(fileName, encoding='utf-8')