import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QSlider, QPushButton, QStackedLayout, QSpinBox, QLineEdit) ##All the widgets I may use I'll import here

class TweetScrape(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mainVLayout = QVBoxLayout()
        self.topHlayout = QHBoxLayout()
        self.mainSLayout = QStackedLayout()


        ##Layouts for different screens
        self.tweetNumW = QWidget()
        self.taregtScrapeW = QWidget()


        self.mainSLayout.addWidget(self.tweetNumW)
        self.currentindex = 0


        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backButton.setIconSize(QSize(40, 40))
        self.backButton.setFixedSize(QSize(40, 40))
        self.backButton.setProperty("class", "settingsButtons")
        self.backButton.clicked.connect(self.back)
        self.welcomeLabel = QLabel("Welcome to the hellscape which is twitter")
        self.welcomeLabel.setProperty("class", "title")
        self.mainVLayout.addWidget(self.backButton)
        self.mainVLayout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignTop)
        self.mainVLayout.addLayout(self.mainSLayout)
        self.setLayout(self.mainVLayout)
        self.tweetNumMenue()
    def tweetNumMenue(self):
        self.tweetNumV = QVBoxLayout()
        self.next = NextButton("NEXT")
        self.next.clicked.connect(self.nextPage)

        self.numL = QLabel("Please enter how many tweets you want to scrape:")
        self.tweetSlide = QSlider(Qt.Orientation.Horizontal)
        self.tweetSlide.setRange(10, 10000)
        self.tweetSlide.setProperty("class", "settingMenueB")
        self.tweetSlide.setPageStep(10)
        self.tweetSlide.valueChanged.connect(self.slideValChnage)
        self.slideNum = QSpinBox()
        self.slideNum.setValue(0)
        self.slideNum.setMaximum(10000)
        self.slideNum.valueChanged.connect(self.slideValChnage)
        self.slideH = QHBoxLayout()
        self.tweetNumV.addWidget(self.numL)
        self.slideH.addWidget(self.tweetSlide)
        self.slideH.addWidget(self.slideNum)

        self.tweetNumV.addLayout(self.slideH)
        self.tweetNumV.addWidget(self.next, alignment=Qt.AlignmentFlag.AlignRight)
        self.tweetNumW.setLayout(self.tweetNumV)
    def taregtScrape(self):
        self.targetSV = QVBoxLayout()
        self.optionH = QHBoxLayout()

        self.accountB = QPushButton("Account")
        self.accountB.setProperty("class", "settingsMenueB")
        self.accountB.setFixedSize(QSize(180, 40))
        self.accountB.setCheckable(True)
        self.accountB.clicked.connect(self.accountOpt)
        self.searchB = QPushButton("Search Term")
        self.optionH.addWidget(self.accountB)
        self.searchB.setFixedSize(QSize(180, 40))
        self.searchB.setProperty("class", "settingsMenueB")
        self.searchB.setCheckable(True)
        self.optionH.addWidget(self.searchB)
        self.textEntry = QLineEdit()

        self.targetSV.addLayout(self.optionH)
        self.optionL = QLabel("Please select what to scrape")
        self.targetSV.addSpacing(10)
        self.targetSV.addWidget(self.optionL)
        self.targetSV.addWidget(self.textEntry)

        self.backNextHL = QHBoxLayout()
        self.next2 = NextButton("NEXT")
        self.backB = NextButton("BACK")
        self.backB.clicked.connect(self.backTweetOption)
        self.backNextHL.addWidget(self.next2, alignment=Qt.AlignmentFlag.AlignRight)
        self.backNextHL.addWidget(self.backB, alignment=Qt.AlignmentFlag.AlignLeft)
        self.targetSV.addLayout(self.backNextHL)
        self.taregtScrapeW.setLayout(self.targetSV)
    def searchOpt(self):
        self.accountB.setChecked(False)
        self.searchB.setChecked(True)
        self.optionL.setText("Please enter your search term:")
    def accountOpt(self):
        self.accountB.setChecked(True)
        self.searchB.setChecked(False)
        self.optionL.setText("Please enter an account name:")
    def slideValChnage(self, val):
        self.slideNum.setValue(val)
        self.tweetSlide.setValue(val)
    def backTweetOption(self):
        self.currentindex -= 1
        self.mainSLayout.setCurrentIndex(self.currentindex)
    def back(self):
        from UI import backButton

        backButton()
    def nextPage(self):
        self.currentindex += 1
        self.taregtScrape()
        self.mainSLayout.addWidget(self.taregtScrapeW)
        self.mainSLayout.setCurrentIndex(self.currentindex)

class NextButton(QPushButton):
    def __init__(self, parent=None):
        super(). __init__(parent)

        self.setFixedSize(QSize(180, 40))
        self.setProperty("class", "menueButtons")