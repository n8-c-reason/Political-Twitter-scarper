import sys ##Allows you to launch the app from commandline 
from threading import Thread
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QComboBox, 
     QHBoxLayout, QLabel, QSlider, QPushButton, QCheckBox, QStackedLayout, QSpinBox, QLineEdit, QGridLayout, QDateEdit, QProgressBar) ##All the widgets I may use I'll import here






class TweetScrape(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        ##Parameters for scrapeing
        self.account = True
        self.numTweets = 0
        self.searchFor = "" ## First is the option. Second is actual string entered by user
        self.fileName = ""
        self.fromDate = QDate()
        self.toDate = QDate()
        ## 1 = account search
        ## 0 = hashtag search

        ##LAYOUTS FOR MAIN SCREEN
        self.mainVLayout = QVBoxLayout()
        self.topHlayout = QHBoxLayout()
        self.mainSLayout = QStackedLayout()


        ##STACKED LAYOUTS FOR OTHER SCREENS
        self.tweetNumW = QWidget()
        self.taregtScrapeW = QWidget()
        self.dataManegemntW = QWidget()
        self.fileNameW = QWidget()
        self.dateTimeEntryW = QWidget()
        self.startScrapeW = QWidget()
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
        self.next.clicked.connect(self.nextPage0)


        ## MAIN WIDGETS FOR TWEET NUM SELECTION
        self.numL = QLabel("Please enter how many tweets you want to scrape:")
        ## The slider to select the number of tweets to scrape
        self.tweetSlide = QSlider(Qt.Orientation.Horizontal)
        self.tweetSlide.setRange(0, 10000)
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
        self.tweetNumV.addSpacing(30)
        self.tweetNumV.addWidget(self.next, alignment=Qt.AlignmentFlag.AlignRight)
        self.tweetNumW.setLayout(self.tweetNumV)

        ## Error pop up when no tweets selected 
        self.tweetNumError = QLabel("Please enter a number of tweets")
        self.tweetNumError.setProperty("class", "error")
    def taregtScrape(self):
        self.termEntered = False
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
        self.textEntry.setEnabled(False)
        self.textEntry.textChanged.connect(self.scrapeTerm)
        self.targetSV.addLayout(self.optionH)
        self.optionL = QLabel("Please select what to scrape")
        self.targetSV.addSpacing(10)
        self.targetSV.addWidget(self.optionL)
        self.targetSV.addWidget(self.textEntry)
        self.targetSV.addSpacing(30)

        ## BACK NEXT BUTTON AND ADDING TO LAYOUTS
        self.backNextHL = QHBoxLayout()
        self.next2 = NextButton("NEXT")
        self.next2.clicked.connect(self.nextPage1)
        self.backB = NextButton("BACK")
        self.backB.clicked.connect(self.backTweetOption)
        self.backNextHL.addWidget(self.backB, alignment=Qt.AlignmentFlag.AlignLeft)
        self.backNextHL.addWidget(self.next2, alignment=Qt.AlignmentFlag.AlignRight)

        self.targetSV.addLayout(self.backNextHL)
        self.taregtScrapeW.setLayout(self.targetSV)

        self.termError = QLabel("Please enter a scrape term")
        self.termError.setProperty("class", "error")
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

        self.usesentiment = QCheckBox("Use sentiment analysis on tweets")
        self.createGraphs = QCheckBox("Create a graph from results")
        self.showSimplitfied = QCheckBox("Show simplified overview of data")

        ## ADD WIDGETS TO LAYOUTS
        self.checkBoxG.addWidget(self.usesentiment, 0,0)
        self.checkBoxG.addWidget(self.createGraphs, 0,1)
        self.checkBoxG.addWidget(self.showSimplitfied, 1,0)

        self.dataMainV.addWidget(self.optionsL)
        self.dataMainV.addLayout(self.comboH)
        self.dataMainV.addLayout(self.checkBoxG)

        self.nextBackH = QHBoxLayout()
        self.next3 = NextButton("NEXT")
        self.next3.clicked.connect(self.nextPage2)
        self.back3 = NextButton("BACK")
        self.back3.clicked.connect(self.backTweetOption)
        self.nextBackH.addWidget(self.back3, alignment=Qt.AlignmentFlag.AlignLeft)
        self.nextBackH.addWidget(self.next3, alignment=Qt.AlignmentFlag.AlignRight)
        self.dataMainV.addLayout(self.nextBackH)

        self.dataManegemntW.setLayout(self.dataMainV)

    def nameFile(self):
        self.nameEntered = False
        self.fileNamV = QVBoxLayout()

        self.fileNamL = QLabel("Please enter a name for the spread sheet file:")
        self.fileNameLE = QLineEdit()
        self.fileNameLE.textChanged.connect(self.fileNameEnterd)
        
        self.fileNamV.addWidget(self.fileNamL)
        self.fileNamV.addWidget(self.fileNameLE)
        
        self.nextbackH1 = QHBoxLayout()
        self.next4 = NextButton("START SCRAPE")
        self.next4.clicked.connect(self.nextPage3)
        self.back3 = NextButton("BACK")
        self.back3.clicked.connect(self.backTweetOption)
        self.nextbackH1.addWidget(self.back3, alignment=Qt.AlignmentFlag.AlignLeft)
        self.nextbackH1.addWidget(self.next4, alignment=Qt.AlignmentFlag.AlignRight)
        self.fileNameW.setLayout(self.fileNamV)
        self.fileNamV.addLayout(self.nextbackH1)

        self.fileNamError = QLabel("Please enter a file name")
        self.fileNamError.setProperty("class", "error")
    def dateTimeEntry(self):
        self.dateV = QVBoxLayout()
        self.dateH = QHBoxLayout()

        ## MAIN WIDGETS 
        self.fromL = QLabel("Please enter what dates to scrape from:")
        self.fromL.setProperty("class", "smallerLabel")
        self.fromD = QDateEdit()
        self.fromD.editingFinished.connect(self.dateFrom)
        self.toL = QLabel("Please enter dates to scrape to:")
        self.toL.setProperty("class", "smallerLabel")
        self.toD = QDateEdit()
        self.toD.editingFinished.connect(self.dateTo)
        
        self.dateH.addWidget(self.fromL)
        self.dateH.addWidget(self.fromD)
        self.dateH.addWidget(self.toL)
        self.dateH.addWidget(self.toD)

        self.dateV.addLayout(self.dateH)
        self.dateTimeEntryW.setLayout(self.dateV)

        self.nextbackH2 = QHBoxLayout()
        self.next5 = NextButton("NEXT")
        self.next5.clicked.connect(self.nextPage4)
        self.back2 = NextButton("BACK")
        self.back2.clicked.connect(self.backTweetOption)
        self.nextbackH2.addWidget(self.back2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.nextbackH2.addWidget(self.next5, alignment=Qt.AlignmentFlag.AlignRight)
        self.dateV.addLayout(self.nextbackH2)

    def startScrape(self):
        self.scrapeV = QVBoxLayout()

        self.scrapeL = QLabel("Your file is being made")
        self.scrapeV.addWidget(self.scrapeL)
        self.startScrapeW.setLayout(self.scrapeV)
        self.scrapeProgress = QProgressBar()
        self.scrapeProgress.setValue(0)
        self.scrapeV.addWidget(self.scrapeProgress)
        self.callScraper(self.numTweets, self.searchFor, self.account, self.fileName, self.fromDate, self.toDate)
    ## CLICKLED CONNECT FUNCTIONS
    ## Toggle btween account and hashtag scrape
    def dateFrom(self):
        value = self.fromD.date()
        value = value.toString("yyyy, MM, dd")
        self.fromDate = value
    def dateTo(self):
        value = self.toD.date()
        value = value.toString("yyyy, MM, dd")
        self.toDate = value
    def scrapeTerm(self, entry):
        if self.textEntry.text():
            self.termEntered = True
        else:
            self.termEntered = False
        self.searchFor = entry
    def fileNameEnterd(self, entry):
        if self.fileNameLE.text():
            self.nameEntered = True
        else:
            self.nameEntered = False
        self.fileName = entry
    def searchOpt(self):
        self.account = False
        self.textEntry.setEnabled(True)
        self.accountB.setChecked(False)
        self.searchB.setChecked(True)
        self.optionL.setText("Please enter your search term:")
    def accountOpt(self):
        self.account = True
        self.textEntry.setEnabled(True)
        self.accountB.setChecked(True)
        self.searchB.setChecked(False)
        self.optionL.setText("Please enter an account name:")
    def nameNeeded(self, state):
        if state == Qt.CheckState.Checked.value:
            self.fileNameNeeded = True
        else:
            self.fileNameNeeded = False
    def slideValChnage(self, val):
        if val > 0:
            self.tweetNumSelected = True
        else:
            self.tweetNumSelected = False
        self.slideNum.setValue(val)
        self.tweetSlide.setValue(val)
        self.numTweets = val
    def backTweetOption(self):
        self.currentindex -= 1
        self.mainSLayout.setCurrentIndex(self.currentindex)
    def back(self):
        from UI import backButton

        backButton()
    def nextPage0(self):
        if self.tweetNumSelected == True:
            self.tweetNumError.hide()
            self.currentindex += 1
            self.taregtScrape()
            self.mainSLayout.addWidget(self.taregtScrapeW)
            self.mainSLayout.setCurrentIndex(self.currentindex)
        else:
            self.tweetNumV.insertWidget(1, self.tweetNumError)
    def nextPage1(self):
        if self.account == False and self.termEntered == True:
            self.currentindex += 1
            self.dateTimeEntry()
            self.mainSLayout.addWidget(self.dateTimeEntryW)
            self.mainSLayout.setCurrentIndex(self.currentindex)
        elif self.termEntered == True:
            self.currentindex +=1
            self.dataManegemnt()
            self.mainSLayout.addWidget(self.dataManegemntW)
            self.mainSLayout.setCurrentIndex(self.currentindex)
        else:
            self.targetSV.addWidget(self.termError)
            self.termError.show()
    def nextPage2(self):      
        self.currentindex += 1
        self.nameFile()
        self.mainSLayout.addWidget(self.fileNameW)
        self.mainSLayout.setCurrentIndex(self.currentindex)

    def nextPage3(self):
        self.currentindex += 1
        self.startScrape()
        self.mainSLayout.addWidget(self.startScrapeW)
        self.mainSLayout.setCurrentIndex(self.currentindex)
    def nextPage4(self):
        self.currentindex += 1
        self.dataManegemnt()
        self.mainSLayout.addWidget(self.dataManegemntW)
        self.mainSLayout.setCurrentIndex(self.currentindex)
    def threadStart(self):
        t1 = Thread(target=self.callScraper)
        t1.start()
    def callScraper(self, tweetNum, search, account, fileName, fromD, toD):
        if account == True:
            from mainScraper import startUserScrape
            
            startUserScrape(tweetNum, search, fileName)
        else:
            from mainScraper import startSearchScrape

            startSearchScrape(tweetNum, search, fileName, fromD, toD)
    def progressUpdate(self, total):
        self.scrapeProgress.setValue(total)




class NextButton(QPushButton):
    def __init__(self, parent=None):
        super(). __init__(parent)

        self.setFixedSize(QSize(180, 40))
        self.setProperty("class", "menueButtons")