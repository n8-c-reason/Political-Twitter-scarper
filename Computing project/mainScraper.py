import snscrape.modules.twitter as sntwitter
import pandas as pd




def startUserScrape(numTweets, search, fileName):
    # Created a list to append all tweet attributes(data)
    attributesContainer = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{search}').get_items()):
        if i>numTweets:
            break
        attributesContainer.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])

        
    # Creating a dataframe from the tweets list above 
    tweetsDF = pd.DataFrame(attributesContainer, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
    fileName = fileName + ".csv"
    tweetsDF.to_csv(fileName, encoding='utf-8')

def startSearchScrape(numTweets, search, fileName, dateFrom, dateTo):
    # Creating list to append tweet data to
    attributesContainer = []

    # Using TwitterSearchScraper to scrape data
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search} since:{dateFrom} until:{dateTo}').get_items()):
        if i>numTweets:
            break
        from UI import progressBarUpdate
        progressBarUpdate(i, numTweets)
        attributesContainer.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweetsDF = pd.DataFrame(attributesContainer, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    fileName = fileName + ".csv"
    tweetsDF.to_csv(fileName, encoding="utf-8")

def scrapeTester(account): ## Used to test if a username exists
    attributesContainer = []
    try: ## Try except to check if there is an error finding username
        for i,tweet in enumerate(sntwitter.TwitterProfileScraper(f'from:{account}').get_items()):
            if i>1:
                break
            attributesContainer.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
            return (True) ## Does not save to file just checks if it works and then will return true
    except:
        return (False)


    