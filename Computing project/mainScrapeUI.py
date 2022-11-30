import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QComboBox, 
     QHBoxLayout, QLabel, QSlider, QPushButton, QCheckBox, QStackedLayout, QSpinBox, QLineEdit, QGridLayout) ##All the widgets I may use I'll import here

class TweetScrape(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        ##Parameters for scrapeing
        self.numTweets = 0
        self.searchFor = (1, "") ## First is the option. Second is actual string entered by user
        ## 1 = account search
        ## 0 = hashtag search

        ##LAYOUTS FOR MAIN SCREEN
        self.mainVLayout = QVBoxLayout()
        self.topHlayout = QHBoxLayout()
        self.mainSLayout = QStackedLayout()


        ##STACKED LAYOUTS FOR OTHER SCREENS
        self.tweetNumW = QWidget()
        self.taregtScrapeW = QWidget()
        self.mainSLayout.addWidget(self.tweetNumW) ## Have to use widgets to add to Stacked layout
        self.currentindex = 0 ##Index to keep track of current screen

        ## MISC WIDGETS FOR MAIN MENUE
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backButton.setIconSize(QSize(40, 40))
        self.backButton.setFixedSize(QSize(40, 40))
        self.backButton.setProperty("class", "settingsButtons")
        self.backButton.clicked.connect(self.back)
        self.welcomeLabel = QLabel("Welcome to the hellscape which is twitter")
        self.welcomeLabel.setProperty("class", "title")

        ##ADD WIDGETS TO LAYOUTS
        self.mainVLayout.addWidget(self.backButton)
        self.mainVLayout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignTop)
        self.mainVLayout.addLayout(self.mainSLayout)
        self.setLayout(self.mainVLayout)

        ## Initiate the first screen
        self.tweetNumMenue()
    def tweetNumMenue(self):
        self.tweetNumSelected = False ## To check if a tweet num has been entered

        ## The main layout for this section
        self.tweetNumV = QVBoxLayout()

        ##The button to continue to the next section
        self.next = NextButton("NEXT")
        self.next.setToolTip("To search term selection")
        self.next.clicked.connect(self.nextPage)


        ## MAIN WIDGETS FOR TWEET NUM SELECTION
        self.numL = QLabel("Please enter how many tweets you want to scrape:")
        ## The slider to select the number of tweets to scrape
        self.tweetSlide = QSlider(Qt.Orientation.Horizontal)
        self.tweetSlide.setRange(10, 10000)
        self.tweetSlide.setProperty("class", "settingMenueB")
        self.tweetSlide.setPageStep(10)
        self.tweetSlide.setToolTip("This is the number of tweets to scrape")
        self.tweetSlide.valueChanged.connect(self.slideValChnage)

        ## This is next to th slide to be changed to exact values 
        self.slideNum = QSpinBox()
        self.slideNum.setValue(0)
        self.slideNum.setMaximum(10000)
        self.slideNum.valueChanged.connect(self.slideValChnage)
        self.slideH = QHBoxLayout() ## The layout which holds the spin box to the right of the slider


        ##ADD WIDGETS TO THE LAYOUTS
        self.tweetNumV.addWidget(self.numL)
        self.slideH.addWidget(self.tweetSlide)
        self.slideH.addWidget(self.slideNum)
        self.tweetNumV.addLayout(self.slideH)
        self.tweetNumV.addWidget(self.next, alignment=Qt.AlignmentFlag.AlignRight)
        self.tweetNumW.setLayout(self.tweetNumV)

        ## Error pop up when no tweets selected 
        self.tweetNumError = QLabel("Please enter a number of tweets")
        self.tweetNumError.setProperty("class", "error")
    def taregtScrape(self):
        ##LAYOUTS FOR THIS LAYOUT
        self.targetSV = QVBoxLayout()
        self.optionH = QHBoxLayout()

        ## BUTTON WIDGETS
        self.accountB = QPushButton("Account")
        self.accountB.setProperty("class", "settingsMenueB")
        self.accountB.setFixedSize(QSize(180, 40))
        self.accountB.setCheckable(True)
        self.accountB.setToolTip("Scrape by one account")
        self.accountB.clicked.connect(self.accountOpt)
        self.searchB = QPushButton("Search Term")
        self.searchB.setToolTip("Search by a hashtag/twitter search")
        self.optionH.addWidget(self.accountB)
        self.searchB.setFixedSize(QSize(180, 40))
        self.searchB.setProperty("class", "settingsMenueB")
        self.searchB.setCheckable(True)
        self.searchB.clicked.connect(self.searchOpt)
        self.optionH.addWidget(self.searchB)

        ## MISC WIDGETS 
        self.textEntry = QLineEdit()
        self.targetSV.addLayout(self.optionH)
        self.optionL = QLabel("Please select what to scrape")
        self.targetSV.addSpacing(10)
        self.targetSV.addWidget(self.optionL)
        self.targetSV.addWidget(self.textEntry)

        ## BACK NEXT BUTTON AND ADDING TO LAYOUTS
        self.backNextHL = QHBoxLayout()
        self.next2 = NextButton("NEXT")
        self.backB = NextButton("BACK")
        self.backB.clicked.connect(self.backTweetOption)
        self.backNextHL.addWidget(self.next2, alignment=Qt.AlignmentFlag.AlignRight)
        self.backNextHL.addWidget(self.backB, alignment=Qt.AlignmentFlag.AlignLeft)
        self.targetSV.addLayout(self.backNextHL)
        self.taregtScrapeW.setLayout(self.targetSV)
    def dataManegemnt(self):
        self.dataMainV = QVBoxLayout()
        self.checkBoxG = QGridLayout()

        ## MAIN SECTION WIDGETS
        self.optionsL = QLabel("Please select the options for your data")
        self.comboH = QHBoxLayout()
        self.csvComboBox = QComboBox()
        self.csvComboBox.addItems(["CSV", "Excel"])
        self.comboLabel = QLabel("What file type to save as")
        self.comboH.addWidget(self.comboLabel)
        self.comboH.addWidget(self.csvComboBox)

        self.saveRawTweets = QCheckBox("Save raw tweets as spread sheet")
        self.usesentiment = QCheckBox("Use sentiment analysis on tweets")
        self.createGraphs = QCheckBox("Create a graph from results")
        self.showSimplitfied = QCheckBox("Show simplified overview of data")


    ## Toggle btween account and hashtag scrape
    def searchOpt(self):
        self.accountB.setChecked(False)
        self.searchB.setChecked(True)
        self.optionL.setText("Please enter your search term:")
    def accountOpt(self):
        self.accountB.setChecked(True)
        self.searchB.setChecked(False)
        self.optionL.setText("Please enter an account name:")
    
    def slideValChnage(self, val):
        if val > 0:
            self.tweetNumSelected = True
        else:
            self.tweetNumSelected = False
        self.slideNum.setValue(val)
        self.tweetSlide.setValue(val)
    def backTweetOption(self):
        self.currentindex -= 1
        self.mainSLayout.setCurrentIndex(self.currentindex)
    def back(self):
        from UI import backButton

        backButton()
    def nextPage(self):
        if self.tweetNumSelected == True:
            self.tweetNumError.hide()
            self.currentindex += 1
            self.taregtScrape()
            self.mainSLayout.addWidget(self.taregtScrapeW)
            self.mainSLayout.setCurrentIndex(self.currentindex)
        else:
            self.tweetNumV.insertWidget(1, self.tweetNumError)

class NextButton(QPushButton):
    def __init__(self, parent=None):
        super(). __init__(parent)

        self.setFixedSize(QSize(180, 40))
        self.setProperty("class", "menueButtons")