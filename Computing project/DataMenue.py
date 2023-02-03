import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton, QLineEdit, QStackedLayout, QCheckBox, QComboBox) ##All the widgets I may use I'll import here

class DataGraph(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.textEntered = ""
        self.mainVLayout = QVBoxLayout()
        self.mainHLayout = QHBoxLayout()
        self.mainSLayout = QStackedLayout() ## Stacked layout for difrent menues with index var
        self.currentIndex = 0
        self.textEntered =""

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



        ## Add Widgets to the layouts
        self.mainVLayout.addWidget(self.backbutton, alignment=Qt.AlignmentFlag.AlignRight.AlignTop)##Aligning the back button to the top right 
        self.mainVLayout.addLayout(self.mainSLayout)
        self.mainHLayout.addWidget(self.backB, alignment=Qt.AlignmentFlag.AlignLeft)
        self.mainHLayout.addWidget(self.nextB, alignment=Qt.AlignmentFlag.AlignRight)
        self.mainVLayout.addLayout(self.mainHLayout)
        self.setLayout(self.mainVLayout)
        self.mainSLayout.addWidget(self.fileNameW)
        self.mainSLayout.addWidget(self.dataW)

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
        self.testTitle = QLabel("Work in progress")
        self.fileNameV.addWidget(self.textL)
        self.fileNameV.addWidget(self.fileLE)

    def dateChoice(self):
        ## Layout for menue
        self.dataV = QVBoxLayout()
        self.dataH = QHBoxLayout()
        self.dataH2 = QHBoxLayout()
        self.dataW.setLayout(self.dataV)

        ##Widgets for the menue 
        self.wordCountC = QCheckBox("Word frequncy")
        self.sentimentC = QCheckBox("Sentiment analysis")
        self.sentimentC.stateChanged.connect(self.sentimentCheck)
        self.dataL = QLabel("What type of sentiment analaysis:")
        self.typeSentimentC = QComboBox()
        self.typeSentimentC.addItems(["VADAR", "MOVIE REVIEWS"])

        ## Add to layouts
        self.dataH.addWidget(self.dataL)
        self.dataH.addWidget(self.typeSentimentC)
        self.dataH2.addWidget(self.wordCountC)
        self.dataH2.addWidget(self.sentimentC)
        self.dataV.addLayout(self.dataH2)
        self.dataV.addLayout(self.dataH)


    def nextPress(self):
        self.currentIndex += 1
        if self.currentIndex == 2:
            from NLP import ProccessedTweets

            ProccessedTweets(self.textEntered)
            self.back()
        else:
            self.mainSLayout.setCurrentIndex(self.currentIndex)
            self.backB.show()
            self.dateChoice()
        
    def backPress(self):
        if self.currentIndex >= 1:
            self.currentIndex -= 1
            self.mainSLayout.setCurrentIndex(self.currentIndex)
        else:
            self.backB.hide()
    def sentimentCheck(self, state):
        if state == Qt.CheckState.Checked:
            self.typeSentimentC.setEnabled(True)
        else:
            self.typeSentimentC.setEnabled(False)

    def textChanged(self, text):
        self.textEntered = text  
    def back(self):
        from UI import backButton

        backButton()

class NextButton(QPushButton):
    def __init__(self, parent=None):
        super(). __init__(parent)

        self.setFixedSize(QSize(180, 40))
        self.setProperty("class", "menueButtons")