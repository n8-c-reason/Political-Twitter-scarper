import sys ##Allows you to launch the app from commandline 
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QPushButton, QLineEdit, QStackedLayout, QCheckBox, QComboBox) ##All the widgets I may use I'll import here

class DataGraph(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        ##Main layouts
        self.mainVLayout = QVBoxLayout()
        self.mainHLayout = QHBoxLayout()
        self.mainSLayout = QStackedLayout() ## Stacked layout for difrent menues with index var
        self.currentIndex = 0
        ##Varibles needed for sending to NLP file
        self.textEntered = ""
        self.textEntered =""
        self.sentimentNeeded = ""
        self.wordFreqNeeded = False

        ##Widgets needed
        self.fileNameW = QWidget() ## Widget for file name entry menu
        self.dataW = QWidget()

        ## Main back button for menue
        self.backbutton = QPushButton()
        self.backbutton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backbutton.setIconSize(QSize(40, 40))
        self.backbutton.setFixedSize(QSize(40, 40))
        self.backbutton.setProperty("class", "settingsButtons")
        self.backbutton.clicked.connect(self.back)
        ## NEXT AND BACK BUTTON 
        self.backNextHL = QHBoxLayout()
        self.nextB = NextButton("NEXT")
        self.nextB.clicked.connect(self.nextPress)
        self.backB = NextButton("BACK")
        self.backB.clicked.connect(self.backPress)
        self.backB.hide()

        ##Title Label
        self.welcomeLabel = QLabel("Data analysis section")
        self.welcomeLabel.setProperty("class", "title")



        ## Add Widgets to the layouts
        self.mainVLayout.addWidget(self.backbutton, alignment=Qt.AlignmentFlag.AlignTop.AlignRight)##Aligning the back button to the top right 
        self.mainVLayout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignTop.AlignCenter)
        self.mainVLayout.addLayout(self.mainSLayout) ## Adding title
        self.mainHLayout.addWidget(self.backB, alignment=Qt.AlignmentFlag.AlignLeft)
        self.mainHLayout.addWidget(self.nextB, alignment=Qt.AlignmentFlag.AlignRight)
        self.mainVLayout.addLayout(self.mainHLayout)
        self.setLayout(self.mainVLayout)
        self.mainSLayout.addWidget(self.fileNameW)
        self.mainSLayout.addWidget(self.dataW)
        
        ##Calls first sub menu
        self.fileNameEntry()

        ## DATA MANIPULATION OPTIONS
    def fileNameEntry(self):
        ## Main layout for menue and add to widget
        self.fileNameV = QVBoxLayout()
        self.fileNameW.setLayout(self.fileNameV)
        ## FILE NAME ENTRY
        self.textL = QLabel("Please enter the csv name:")
        ## Main entry for the filename
        self.fileLE = QLineEdit()
        self.fileLE.textChanged.connect(self.textChanged)
        self.fileNameV.addWidget(self.textL)
        self.fileNameV.addWidget(self.fileLE)

    def dateChoice(self):
        ## Layout for menue
        self.dataV = QVBoxLayout()
        self.dataH = QHBoxLayout()
        self.dataH2 = QHBoxLayout()
        ##Add to main widget
        self.dataW.setLayout(self.dataV)

        ##Widgets for the menue 
        ##Check boxes needed
        self.wordCountC = QCheckBox("Word frequncy")
        self.wordCountC.stateChanged.connect(self.wordFreqCheck)
        self.sentimentC = QCheckBox("Sentiment analysis")
        self.sentimentC.stateChanged.connect(self.sentimentCheck)
        self.dataL = QLabel("What type of sentiment analaysis:")
        ##Combo box for different sentiment options
        self.typeSentimentC = QComboBox()
        self.typeSentimentC.addItems(["VADAR", "MOVIE REVIEWS"])
        ##Enabled unless a check box is checked
        self.typeSentimentC.setEnabled(False)

        ## Error message
        self.errorLabel = QLabel("Please select atleast one option")
        self.errorLabel.setProperty("class", "error")

        ## Add to layouts
        self.dataH.addWidget(self.dataL)
        self.dataH.addWidget(self.typeSentimentC)
        self.dataH2.addWidget(self.wordCountC)
        self.dataH2.addWidget(self.sentimentC)
        self.dataV.addLayout(self.dataH2)
        self.dataV.addLayout(self.dataH)

    def nextPress(self):
        ##Signle next function
        self.currentIndex += 1 ## Increment index
        if self.currentIndex == 2: ## Checks if last menu
            ##checks if a check box has been checked
            if self.wordFreqNeeded == True or self.sentimentNeeded == "VADER" or self.sentimentNeeded == "MOVIE":
                ##Calls the class from the NLP file
                from NLP import ProccessedTweets

                ProccessedTweets(self.textEntered, self.wordFreqNeeded, self.sentimentNeeded)
                ##Returns to the main menu
                self.back()
            else:
                ##Displays the error label if nothing is selected 
                self.dataV.addWidget(self.errorLabel)
        else:
            ##Shows back button when on last submenu
            self.mainSLayout.setCurrentIndex(self.currentIndex)
            self.backB.show()
            self.dateChoice()
    
    def backPress(self):
        ##Takes the index back one and hides the back button
        self.currentIndex -= 1
        self.mainSLayout.setCurrentIndex(self.currentIndex)

        self.backB.hide()
    def wordFreqCheck(self, state):
        ##If it has been checked it changes the varible 
        if state == 2: ## 2 == checked
            self.wordFreqNeeded = True
        else:
            self.wordFreqNeeded = False
    def sentimentCheck(self, state):
        if state == 2:
            ##Enables the combo box
            self.typeSentimentC.setEnabled(True)
            self.sentimentNeeded = "VADER"
        else:
            self.typeSentimentC.setEnabled(False)
            self.sentimentNeeded = ""

    def textChanged(self, text):
        ##Updates the varible 
        self.textEntered = text  
    def back(self):
        ##Takes back to main menu
        from UI import backButton

        backButton()
##Class for creating buttons
class NextButton(QPushButton):
    def __init__(self, parent=None):
        super(). __init__(parent)

        self.setFixedSize(QSize(180, 40))
        self.setProperty("class", "menueButtons")