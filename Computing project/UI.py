import sys ##Allows you to launch/exit the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QStackedLayout) ##All the widgets I may use I'll import here

##Import other classes from different python files
from Settingsmenue import SettingsMenue 
from PrimaryMenue import PrimaryMenue
from EmailMenue import EmailData
from DataMenue import DataGraph
from mainScrapeUI import TweetScrape

##FUNCTIONS FOR WINDOW CHANGE
## This will allow me to widgets I've added to the stack and index it aacordilngly to it
currentIndexMain = 0
def changeScrape():
    ##Scrape menu change
    global mainStackLayout, currentIndexMain, scrapeM
    ##Create the object
    scrapeM = TweetScrape()
    ##Add to s layout
    mainStackLayout.addWidget(scrapeM)
    ##Increment index
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeSettings():
    ##Setting menu change
    global mainStackLayout, currentIndexMain
    settingM = SettingsMenue()
    mainStackLayout.addWidget(settingM)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeEmail():
    ##Email menu change
    global mainStackLayout, currentIndexMain
    emailD = EmailData()
    mainStackLayout.addWidget(emailD)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeData():
    ##Data menu change
    global mainStackLayout, currentIndexMain
    dataG = DataGraph()
    mainStackLayout.addWidget(dataG)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)

##MISC functions
def progressBarUpdate(value, total):
    totalProg = (value/total)*100
    totalProg.round()
    scrapeM.progressUpdate(total)

def settingsReset(): ##When changing anything in stylesheet it needs to be reapplied 
    with open(os.path.join(sys.path[0], "main style sheet.qss"), "r+") as f: 
        _style = f.read() 
        app.setStyleSheet(_style)##Sets the style sheet

def backButton(): ## this can be called when going back a menue
    mainStackLayout.setCurrentIndex(0)



##creates the one application I'll use for my project
app = QApplication(sys.argv) ##An object which holds the event loop

##Main widget for whole app
widgets = QWidget()

##Main stacked layout for main widget
mainStackLayout = QStackedLayout()
##Setting the s layout to the widget
widgets.setLayout(mainStackLayout)

##initiating the first menu
firstMenue = PrimaryMenue()
mainStackLayout.addWidget(firstMenue)
##Sizing the window
widgets.setFixedHeight(450)
widgets.setFixedWidth(600)
##Icon for app and title
widgets.setWindowIcon(QIcon("Computing project\Images\icons8-twitter-26.png"))
widgets.setWindowTitle("Tweet analysier")

widgets.show()##All widgets need to be shown

## Opens the main style sheet for the project
with open(os.path.join(sys.path[0], "main style sheet.qss"), "r+") as f: 
    _style = f.read() 
    app.setStyleSheet(_style)##Sets the style sheet

##Starts the loop
if __name__ == '__main__': ##Starts the program
    app.exec()
