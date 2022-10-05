from cgi import test
import sys ##Allows you to launch the app from commandline 
import os
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
        self._height = 450 # change these if needed. currently there in the ratio 4:3 
        self._length = 600
        self.setFixedHeight(self._height)
        self.setFixedWidth(self._length)

        #Orignally I would have used the font in my stylesheet but @font-faces does not work
        fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Arvo-Regular.ttf") ##This loads the font from the local location
        self.families = QFontDatabase.applicationFontFamilies(fontId) ## This allows me to have a dictionary of fonts
        fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Tahoma Regular font.ttf")

        self.primaryMenue()## Calls the function for the primary menue

        self.setCentralWidget(self.mainWidget) ## Sets the the window to the primary menue through the main widget
        ##change this if you want to change menue ^

    def primaryMenue(self):## The function which will hold all the widgets for the primary menue
        ##Creates the layout which I'll use to store my widgets
        self.mainVLayout = QVBoxLayout()

        ## QLABEL ##
        self.centralTitle = QLabel("Tweet sentiment analysier") ##Creates a Qlabel which I'll use for my main title
        self.centralTitle.setProperty("class", "title") ## This applies the class from my stylesheet to this widget
        self.centralTitle.setFont(QFont("Arvo")) ## Sets the font for this widget to Arvo

        ## QPUSHBUTTON ##
        self.tweetScraping = Button("Tweet scraping", "tweetSFunc")

        self.retriveData = Button("Retrive Data", "retriveDFunc")

        self.loadData = Button("Load Data", "loadDFunc")

        self.emailData = Button("Email Data", "emailDFunc")
        
        ## ADD WIDGETS TO LAYOUT ##
        self.mainVLayout.addSpacing(20) ## Creates a gap above the label
        self.mainVLayout.addWidget(self.centralTitle)##Adds the label to the layout at the postion (2)
        self.mainVLayout.addSpacing(10)
        ##This is where I attach all my buttons to the layout and then alignes them using the alingment flag tool
        self.mainVLayout.addWidget(self.tweetScraping, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.retriveData, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.loadData, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.emailData, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mainWidget = QWidget()  ## This creates the widget which holds the primary menue
        self.mainWidget.setLayout(self.mainVLayout) ## This attaches the layout to this widget

        ## Ther first alignes the label to the top and the second centers the whole V layout.
        self.centralTitle.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainVLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    def tweetSFunc(self):
        print("test3")

## The class which I use to create my buttons. Pyqt you have to do this with classes like if you were to do it in tkinter with functions
class Button(QPushButton):
    def __init__(self, parent=None, functionName=""): ##I need to know the name for button and what function it will call when clicked
        super().__init__(parent)

        self.functionName = functionName
        
        self.setProperty("class", "menueButtons")##This aplies the class from my stylesheet to the widget
        self.setFont(QFont("Tahoma")) ## Sets the font from the dictionary 
        self.setFixedSize(QSize(120, 45)) ## The set size of the button (widpth, hight)
        self.setChecked(True)
        self.clicked.connect(self.buttonFunction) ##This says that when the button is clicked that it will run that function

    def tweetSFunc(self):
        ## This then calls the function in my main window class so that I can change things easily there
        method = MainWindow().tweetSFunc
        method()

    def buttonFunction(self):
        exec("self." + (self.functionName) + "()") ## This makes funtionName a runable function call with exec.


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
