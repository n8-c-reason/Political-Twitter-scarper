import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton, QLineEdit) ##All the widgets I may use I'll import here

class DataGraph(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.textEntered = ""
        self.mainVLayout = QVBoxLayout()
        self.backbutton = QPushButton()
        self.backbutton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backbutton.setIconSize(QSize(40, 40))
        self.backbutton.setFixedSize(QSize(40, 40))
        self.backbutton.clicked.connect(self.back)

        ## File name entry
        self.textL = QLabel("Please enter the csv name:")
        self.fileNameEntry = QLineEdit()
        self.fileNameEntry.textChanged.connect(self.textChanged)
        self.enterB = QPushButton("NEXT")
        self.enterB.setFixedSize(QSize(180, 40))
        self.enterB.setProperty("class", "menueButtons")
        self.enterB.clicked.connect(self.)
        self.testTitle = QLabel("Work in progress")
        self.mainVLayout.addWidget(self.backbutton, alignment=Qt.AlignmentFlag.AlignRight.AlignTop)
        self.mainVLayout.addWidget(self.testTitle)
        self.setLayout(self.mainVLayout)
    def textChanged(self, text):
        self.textEntered = text
    def enterMap(self):
        from NLP import ProccessedTweets

        ProccessedTweets(self.textEntered)       
    def back(self):
        from UI import backButton

        backButton()