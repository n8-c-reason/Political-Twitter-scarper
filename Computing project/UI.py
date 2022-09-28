import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout) ##All the widgets I may use I'll import here


##This is the subclass for our QMain window
class MainWindow(QMainWindow):##Everything will be contained within this widget.
    def __init__(self): ##When you make a subclass for a Qt class we always need to call a super init function
        ##This alows Qt to create an object
        super().__init__()

        ##This allows us to change the title of our window
        self.setWindowTitle("Python Twitter scraper")##This is aimed at self(MainWindow)

        self.primaryMenue()## Calls the function for the primary menue

        self.setCentralWidget(self.mainWidget) ## Sets the the window to the primary menue through the main widget
        ##change this if you want to change menue ^

    def primaryMenue(self):## The function which will hold all the widgets for the primary menue
        ##The layout I shall use for this menue is the gridlayout
        self.gMainLayout = QGridLayout()##This allows me to split my window in to multile pices

        self.centralTitle = QLabel("Tweet sentiment analysier c") ##Creates a Qlabel which I'll use for my main title
        self.centralTitle.setProperty("class", "title")
        self.gMainLayout.addWidget(self.centralTitle, 3,3)##Adds the label to the layout at the postion (3,3)

        self.mainWidget = QWidget()  ## This creates the widget which holds the primary menue
        self.mainWidget.setLayout(self.gMainLayout) ## This attaches the layout to this widget






        


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
