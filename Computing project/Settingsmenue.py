import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QCheckBox, QPushButton, QStackedLayout, QSpinBox)
from pip import main ##All the widgets I may use I'll import here


class SettingsMenue(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent) ## We can set the parent 
        self.mainVLayout = QVBoxLayout() ## This is the main layout for the page
        self.mainHLayout = QHBoxLayout() ## This holds the buttons for the two settings menue
        self.mainSLayouts = QStackedLayout() ## This layout allows us to switch between are to layouts

        ##MAIN BUTTON WIDGETS
        self.tweetLabel = QPushButton("Tweet scraping", self) ## This button chall be at the top with the other
        self.tweetLabel.setFixedSize(QSize(180, 40)) ## Use this to resize your buttons widpth,height
        self.tweetLabel.setProperty("class", "settingsMenueB") ## Sets the class from out qss stylesheet
        self.tweetLabel.clicked.connect(self.changeToTSettings) ## calls the function when clicked
        self.tweetLabel.setCheckable(True)
        self.accessLabel = QPushButton("Accesibilty")
        self.accessLabel.setFixedSize(QSize(180, 40))
        self.accessLabel.setProperty("class", "settingsMenueB")
        self.accessLabel.clicked.connect(self.changeToAccess)
        self.accessLabel.setCheckable(True)

        self.backButton = QPushButton() ## This back button uses an icon 
        self.backButton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backButton.setProperty("class", "settingsButtons") 
        self.backButton.setFixedSize(QSize(40, 40))
        self.backButton.setIconSize(QSize(40, 40))
        self.backButton.clicked.connect(self.back) ## It then calls a fucntion which will then change the index back to the main menue

        ## ADD WIDGETS TO LAYOUTS
        self.mainHLayout.addSpacing(100) ## This is so there centered close in the middle
        self.mainHLayout.addWidget(self.accessLabel, alignment=Qt.AlignmentFlag.AlignLeading) ## This then justifys them so they are centered equaly
        self.mainHLayout.addWidget(self.tweetLabel, alignment=Qt.AlignmentFlag.AlignTrailing)
        self.mainHLayout.addSpacing(100)
        self.mainVLayout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.mainVLayout.addLayout(self.mainHLayout)
        self.mainVLayout.addLayout(self.mainSLayouts)

        ##ACCESIBILTY MENUE
        self.accessWidget = QWidget() ## THe widget used for that setting menue
        self.accessVLayout = QVBoxLayout()
        self.textSizeHLayout = QHBoxLayout() ## Horizontal layout for each row. I shall explore using a grid layout if thats better
        self.textSize = Labels("Font size", 13)
        self.numEntry = QSpinBox()
        self.numEntry.valueChanged.connect(self.textChnaged)

        self.colourHLayout = QHBoxLayout()
        self.darkMode = QCheckBox("Dark Mode", self)
        self.systemColours = Labels("System Colours", 13)
        self.textSizeHLayout.addWidget(self.textSize)
        self.textSizeHLayout.addWidget(self.numEntry)
        self.accessVLayout.addLayout(self.textSizeHLayout)
        self.accessWidget.setLayout(self.accessVLayout)
        self.accessVLayout.addWidget(self.systemColours)
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
        self.tweetLabel.setChecked(False)
    def changeToTSettings(self):
        self.mainSLayouts.setCurrentIndex(1)
        self.accessLabel.setChecked(False)
    def textChnaged(self, newVal):
        print(newVal)
        if newVal > 35:
            self.error = QLabel("Maxium fontzize of 30")
            self.accessVLayout.addWidget(self.error)
            self.error.setProperty("class", "error")
        else:
            try:
                self.error.hide()
            except:
                with open(os.path.join(sys.path[0], "main style sheet.qss"), "r") as f:
                        css = f.readlines()
                css[1] = (f"    font-size: {newVal}px;\n")
                css[4] = (f"    font-size: {newVal}px;\n")
                with open(os.path.join(sys.path[0], "main style sheet.qss"), "w") as f:
                    f.writelines(css)
                from UI import settingsReset
                settingsReset()                

    def back(self):
        from UI import backButton ## This imports the main file

        backButton() ## Then calls the fucntion to go back
class Labels(QLabel):
    def __init__(self, parent=None, fontSize = 0):
        super().__init__(parent)
        self.setProperty("class", "settingsLabels")