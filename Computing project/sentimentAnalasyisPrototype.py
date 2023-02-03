import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv("test4.csv")
df.head()
class VADARsentiment():
    def __init__(self, df) -> None:
        super().__init__()
        ## Create an instance of the anayliser
        self.sentAnlyiser = SentimentIntensityAnalyzer()
        self.results()
    def polarityCalc(self, output):
        ## Turn the interger polarity in to either negatiove or postive 

        ## If a suffiecent polarity is not met then it will stay neutral
        self.polarity = "neutral"

        ## There is the space between -0.05 and 0.05 where it is neutral
        if(output['compound']>= 0.05):
            self.polarity = "positive"

        elif(output['compound']<= -0.05):
            self.polarity = "negative"

        return self.polarity

    def predictSentiment(self, text):
        ## calls the sentiment analyiser
        output =  self.sentAnlyiser.polarity_scores(text)

        ## Returns the output to the function which turns it in to strings
        return self.polarityCalc(output)
    def results(self):
        ## Creates a new coloumn with the results of the scraper
        df["VADAR predictions"] = df["Tweets"].apply(self.predictSentiment)
        print(df.sample(5))
        ## Calls the plot graph function
        self.plotGraph()
    def plotGraph(self):
        ## Count the number of times the result apears so we can plot the graph
        self.pos = df["VADAR predictions"].value_counts()["positive"]
        self.neg = df["VADAR predictions"].value_counts()["negative"]
        self.neu = df["VADAR predictions"].value_counts()["neutral"]

        ## Add ther values to a numpy array
        self.values = np.array([self.pos, self.neg, self.neu])
        ## Create the array of strings for the titles 
        self.Labels = ["Positive Tweets", "Negative Tweets", "Neutral Tweets"]

        ## Create the pie chart and insert all the needed values
        plt.pie(self.values, labels=self.Labels, shadow = True)
        plt.show()

sentiment = VADARsentiment(df)