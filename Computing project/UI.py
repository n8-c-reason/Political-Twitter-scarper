import sys ##Allows you to launch the app from commandline 
import os
import sass
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

currentIndex = 0## This will allow me to widgets I've added to the stack and index it aacordilngly to it
def changeScrape():
    global mainStackLayout, currentIndex
    scrapeM = TweetScrape()
    mainStackLayout.addWidget(scrapeM)
    currentIndex += 1
    mainStackLayout.setCurrentIndex(currentIndex)
def changeSettings():
    global mainStackLayout, currentIndex
    settingM = SettingsMenue()
    mainStackLayout.addWidget(settingM)
    currentIndex += 1
    mainStackLayout.setCurrentIndex(currentIndex)
def changeEmail():
    global mainStackLayout, currentIndex
    emailD = EmailData()
    mainStackLayout.addWidget(emailD)
    currentIndex += 1
    mainStackLayout.setCurrentIndex(currentIndex)
def changeData():
    global mainStackLayout, currentIndex
    dataG = DataGraph()
    mainStackLayout.addWidget(dataG)
    currentIndex += 1
    mainStackLayout.setCurrentIndex(currentIndex)

##MISC functions

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
