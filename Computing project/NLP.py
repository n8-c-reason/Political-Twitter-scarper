import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import collections
import itertools
import matplotlib.pyplot as plt

def removeUrl(tweet):
    ##reaplace any urls found in the string with nothing
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())


class ProccessedTweets():
    def __init__(self, filename) -> None:
        super().__init__()
        self.openTweets(filename)
        self.tweetsNoURLS = [] ## First stage
        self.wordsInTweets = [] ## Second stage


    def openTweets(self, filename):
        self.df = pd.read_csv(f"{filename}.csv")
        self.noURL()
    def noURL(self):
        for name, values in self.df[['Tweets']].iteritems():
            df["TweetsNoURL"] = [removeUrl(x) for x in values]
        
    def lowerWords(self):
        self.wordsInTweets = [tweet.lower().split() for tweet in self.tweetsNoURLS]
    def countFreq(self):
        self.allwords_ = list(itertools.chain(*wordsInTweets))
        self.countWords_ = collections.Counter(self.allwords_)
        self.tweetWords = pd.DataFrame(countWords.most_common(20), columns=["Words", "Count"])
        self.tweetWords.head()

    def drawGraph(self):
        fig, ax = plt.subplots(figsize = (8, 8))
        # Plot horizontal bar graph
        self.tweetWords.sort_values(by='Count').plot.barh(x='Words',
                            y='Count',
                            ax=ax,
                            color="purple")

        ax.set_title("Common Words Found in Tweets (Including All Words)")

        plt.show()


tweetsNoURLS = []
df =pd.read_csv("test1.csv")
for name, values in df[['Tweets']].items():
    for x in values:
        tweetsNoURLS.append(removeUrl(x))
    df["TweetsNoURL"] = tweetsNoURLS
wordsInTweets = [tweet.lower().split() for tweet in tweetsNoURLS]
allWords = list(itertools.chain(*wordsInTweets))
countWords = collections.Counter(allWords)
tweetWord = pd.DataFrame(countWords.most_common(20), columns = ["Words", "Count"])
tweetWord.head()

# fig, ax = plt.subplots(figsize=(8, 8))

# # Plot horizontal bar graph
# tweetWord.sort_values(by='Count').plot.barh(x='Words',
#                       y='Count',
#                       ax=ax,
#                       color="purple")

# ax.set_title("Common Words Found in Tweets (Including All Words)")

# plt.show()

stop_words = set(stopwords.words('english'))

# View a few words from the set
list(stop_words)[0:10]

tweets_nsw = [[word for word in tweet_words if not word in stop_words]
              for tweet_words in wordsInTweets]

all_words_nsw = list(itertools.chain(*tweets_nsw))

counts_nsw = collections.Counter(all_words_nsw)



cleanTweetsdf = pd.DataFrame(counts_nsw.most_common(20), columns = ["Words", "Count"])
cleanTweetsdf.head()

fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
cleanTweetsdf.sort_values(by='Count').plot.barh(x='Words',
                      y='Count',
                      ax=ax,
                      color="purple")

ax.set_title("Common Words Found in Tweets (Withouth stop words)")

plt.show()


