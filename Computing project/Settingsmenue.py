import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton, QStackedLayout)
from pip import main ##All the widgets I may use I'll import here


class SettingsMenue(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent) ## We can set the parent 
        self.mainVLayout = QVBoxLayout() ## This is the main layout for the page
        self.mainHLayout = QHBoxLayout() ## This holds the buttons for the two settings menue
        self.mainSLayouts = QStackedLayout() ## This layout allows us to switch between are to layouts

        ##MAIN BUTTON WIDGETS
        self.tweetLabel = QPushButton("Tweet scraping") ## This button chall be at the top with the other
        self.tweetLabel.setFixedSize(QSize(180, 40)) ## Use this to resize your buttons widpth,height
        self.tweetLabel.setProperty("class", "settingsMenueB") ## Sets the class from out qss stylesheet
        self.tweetLabel.clicked.connect(self.changeToTSettings) ## calls the function when clicked
        self.accessLabel = QPushButton("Accesibilty")
        self.accessLabel.setFixedSize(QSize(180, 40))
        self.accessLabel.setProperty("class", "settingsMenueB")
        self.accessLabel.clicked.connect(self.changeToAccess)
        self.backButton = QPushButton()
        



        self.mainHLayout.addSpacing(100) ## This is so there centered close in the middle
        self.mainHLayout.addWidget(self.accessLabel, alignment=Qt.AlignmentFlag.AlignLeading) ## This then justifys them so they are centered equaly
        self.mainHLayout.addWidget(self.tweetLabel, alignment=Qt.AlignmentFlag.AlignTrailing)
        self.mainHLayout.addSpacing(100)
        self.mainVLayout.addLayout(self.mainHLayout)
        self.mainVLayout.addLayout(self.mainSLayouts)

        ##ACCESIBILTY MENUE
        self.accessWidget = QWidget() ## THe widget used for that setting menue
        self.accessVLayout = QVBoxLayout()
        self.textSizeHLayout = QHBoxLayout() ## Horizontal layout for each row. I shall explore using a grid layout if thats better
        self.textSize = Labels("Font size", 13)
        self.systemColours = Labels("System Colours", 13)
        self.textSizeHLayout.addWidget(self.textSize)
        self.accessVLayout.addLayout(self.textSizeHLayout)
        self.accessWidget.setLayout(self.accessVLayout)
        self.mainSLayouts.addWidget(self.accessWidget) ## You  can not add a layout to a stacked layout so creating a widget is the way around this
        
        ##TWEET SCRAPING SETTINGS 
        self.tSettingWidget = QWidget()
        self.tSettingVLayout = QVBoxLayout()
        self.test = QLabel("TEST")
        self.tSettingVLayout.addWidget(self.test)
        self.tSettingWidget.setLayout(self.tSettingVLayout)
        self.mainSLayouts.addWidget(self.tSettingWidget)

        self.setLayout(self.mainVLayout)
    def changeToAccess(self):
        self.mainSLayouts.setCurrentIndex(0)
    def changeToTSettings(self):
        self.mainSLayouts.setCurrentIndex(1)
class Labels(QLabel):
    def __init__(self, parent=None, fontSize = 0):
        super().__init__(parent)
        self.setProperty("class", "settingsLabels")