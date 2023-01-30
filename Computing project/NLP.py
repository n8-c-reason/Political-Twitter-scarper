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
        self.tweetsNoStop = []


    def openTweets(self, filename):
        self.df = pd.read_csv(f"{filename}.csv")
        self.noURL()
    def noURL(self):
        for name, values in self.df[['Tweets']].items():
            for x in values:
                self.tweetsNoURLS.append(removeUrl(x))
            df["TweetsNoURL"] = [removeUrl(x) for x in values]
        self.lowerWords()
    def lowerWords(self):
        self.wordsInTweets = [tweet.lower().split() for tweet in self.tweetsNoURLS]
        self.removeStopWords
    def countFreq(self):
        self.allwords_ = list(itertools.chain(*wordsInTweets))
        self.countWords_ = collections.Counter(self.allwords_)
        self.tweetWords = pd.DataFrame(countWords.most_common(20), columns=["Words", "Count"])
        self.tweetWords.head()

    def removeStopWords(self):
        self.stopWords_ = set(stopwords.words('english'))
        self.tweetsNoStop = [[word for word in words if not word in self.stopWords_]for words in self.wordsInTweets]


#     def openAndProccess(self, filename):
#         testTweets = pd.read_csv(filename+".csv")
#         tweets


tweetsNoURLS = []
df =pd.read_csv("test4.csv") ## Read csv

for name, values in df[['Tweets']].items(): ## Read the one row of the df
    for x in values:
        tweetsNoURLS.append(removeUrl(x)) ## Append to the list
    df["TweetsNoURL"] = tweetsNoURLS ## Create a new list in the df

wordsInTweets = [tweet.lower().split() for tweet in tweetsNoURLS] ## Make words lower case
stopword = set(stopwords.words("english"))

tweetnostop = [[word for word in words if not word in stopword]for words in wordsInTweets]

allWords = list(itertools.chain(*tweetnostop))## Create a list of separate words

countWords = collections.Counter(allWords) ## Use the collections module to count words

print(countWords.most_common(30))
## Create a new df with the counts of words
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

## Plot horizontal bar graph
tweetWord.sort_values(by='Count').plot.barh(x='Words',
                      y='Count',
                      ax=ax,
                      color="purple")

ax.set_title("Common Words Found in Tweets (Withouth stop words)")

plt.show()
