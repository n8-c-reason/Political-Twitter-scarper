import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton, QStackedWidget, QStackedLayout) ##All the widgets I may use I'll import here

##Import other classes from different python files
from Settingsmenue import SettingsMenue 
from PrimaryMenue import PrimaryMenue
from EmailMenue import EmailData
from DataMenue import DataGraph
from mainScrapeUI import TweetScrape
##FUNCTIONS FOR WINDOW CHANGE

currentIndexMain = 0## This will allow me to widgets I've added to the stack and index it aacordilngly to it
def changeScrape():
    global mainStackLayout, currentIndexMain, scrapeM
    scrapeM = TweetScrape()
    mainStackLayout.addWidget(scrapeM)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeSettings():
    global mainStackLayout, currentIndexMain
    settingM = SettingsMenue()
    mainStackLayout.addWidget(settingM)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeEmail():
    global mainStackLayout, currentIndexMain
    emailD = EmailData()
    mainStackLayout.addWidget(emailD)
    currentIndexMain += 1
    mainStackLayout.setCurrentIndex(currentIndexMain)
def changeData():
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

widgets = QWidget()
mainStackLayout = QStackedLayout()
widgets.setLayout(mainStackLayout)
firstMenue = PrimaryMenue()
mainStackLayout.addWidget(firstMenue)
widgets.setFixedHeight(450)
widgets.setFixedWidth(600)
widgets.setWindowIcon(QIcon("Computing project\Images\icons8-twitter-26.png"))
widgets.setWindowTitle("Tweet analysier")

widgets.show()##All widgets need to be shown

## Opens the main style sheet for the project
with open(os.path.join(sys.path[0], "main style sheet.qss"), "r+") as f: 
    _style = f.read() 
    app.setStyleSheet(_style)##Sets the style sheet

##Starts the loop
app.exec()

# if __name__ == '__main__': ##Starts the program
#     start()
