import pandas as pd

import nltk as stopwords

from nltk.tokenize import RegexpTokenizer

df = pd.read_csv(r"C:\Users\nates\New folder\Political-Twitter-scarper\test2.csv")
df.head(3)
df.info()
df["Tweets"] = df["Tweets"].str.lower()
df.head(3)
regexp = RegexpTokenizer("/w+")
df["Tweets.token"] = []
df["Tweets.token"] = df["Tweets"].apply(regexp.tokenize)
df.head(3)
