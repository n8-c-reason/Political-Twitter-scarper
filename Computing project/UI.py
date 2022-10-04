from ctypes import alignment
import sys ##Allows you to launch the app from commandline 
import os
from tkinter import font
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton) ##All the widgets I may use I'll import here


##This is the subclass for our QMain window
class MainWindow(QMainWindow):##Everything will be contained within this widget.
    def __init__(self): ##When you make a subclass for a Qt class we always need to call a super init function
        ##This alows Qt to create an object
        super().__init__()

        ##This allows us to change the title of our window
        self.setWindowTitle("Python Twitter scraper")##This is aimed at self(MainWindow)

        #this determines the hieght and width of my program
        self._height = 300 # change these if needed. currently there in the ratio 4:3 
        self._length = 400
        self.setFixedHeight(self._height)
        self.setFixedWidth(self._length)

        #Orignally I would have used the font in my stylesheet but @font-faces does not work
        fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Arvo-Regular.ttf")
        self.families = QFontDatabase.applicationFontFamilies(fontId) ## This allows me to have a dictionary of fonts
        fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Tahoma Regular font.ttf")
        #fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Tahoma Regular font.ttf")
        #self.families = QFontDatabase.applicationFontFamilies(fontId)

        self.primaryMenue()## Calls the function for the primary menue

        self.setCentralWidget(self.mainWidget) ## Sets the the window to the primary menue through the main widget
        ##change this if you want to change menue ^

    def primaryMenue(self):## The function which will hold all the widgets for the primary menue
        ##Creates the layout which I'll use to store my widgets
        self.mainVLayout = QVBoxLayout()

        ## QLABEL
        self.centralTitle = QLabel("Tweet sentiment analysier") ##Creates a Qlabel which I'll use for my main title
        self.centralTitle.setProperty("class", "title")
        self.centralTitle.setFont(QFont("Arvo"))

        ## QPUSHBUTTON
        self.tweetScraping = QPushButton("Tweet scraping")
        self.tweetScraping.setFont(QFont("Tahoma"))
        self.tweetScraping.setProperty("class", "menueButtons")
        self.tweetScraping.setFixedSize(QSize(120, 45))

        self.retriveData = QPushButton("Retrive Data")
        self.retriveData.setProperty("class", "menueButtons")
        self.retriveData.setFont(QFont("Tahoma"))
        self.retriveData.setFixedSize(QSize(120, 45))

        self.loadData = QPushButton("Load Data")
        self.loadData.setProperty("class", "menueButtons")
        self.loadData.setFont(QFont("Tahoma"))
        self.loadData.setFixedSize(QSize(120, 45))

        self.emailData = QPushButton("Email Data")
        self.emailData.setProperty("class", "menueButtons")
        self.emailData.setFont(QFont("Tahoma"))
        self.emailData.setFixedSize(QSize(120, 45))
        
        ##ADD WIDGETS TO LAYOUT
        self.mainVLayout.addSpacing(20) ## Creates a gap above the label
        self.mainVLayout.addWidget(self.centralTitle)##Adds the label to the layout at the postion (2)
        self.mainVLayout.addWidget(self.tweetScraping, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.retriveData, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.loadData, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.emailData, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mainWidget = QWidget()  ## This creates the widget which holds the primary menue
        self.mainWidget.setLayout(self.mainVLayout) ## This attaches the layout to this widget

        ## Ther first alignes the label to the top and the second centers the whole V layout.
        self.centralTitle.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainVLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        


if __name__ == '__main__': ##Starts the program

    ##creates the one application I'll use for my project
    app = QApplication(sys.argv) ##An object which holds the event loop

    ##Creates my first  top level widget widnow
    mainMenue = MainWindow() ## In this case it is QMainWindow

    mainMenue.show() ##All widgets need to be shown
    
    ## Opens the main style sheet for the project
    with open(os.path.join(sys.path[0], "main style sheet.qss"), "r") as f: 
        _style = f.read() 
        app.setStyleSheet(_style)##Sets the style sheet

    ##Starts the loop
    app.exec()
