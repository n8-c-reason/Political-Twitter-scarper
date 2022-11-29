import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton) ##All the widgets I may use I'll import here
from Settingsmenue import SettingsMenue



class PrimaryMenue(QWidget):## The function which will hold all the widgets for the primary menue
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        ##Creates the layout which I'll use to store my widgets
        self.mainVLayout = QVBoxLayout()

        #I know need to create a horizontal layout for my settings and back button to go along the top of the screen
        self.topHLayout = QHBoxLayout()

        ## QLABEL ##
        self.centralTitle = QLabel("        Tweet sentiment analysier        ") ##Creates a Qlabel which I'll use for my main title
        self.centralTitle.setProperty("class", "title") ## This applies the class from my stylesheet to this widget
        self.centralTitle.setFont(QFont("Arvo")) ## Sets the font for this widget to Arvo

        ## QPUSHBUTTON ##
        self.tweetScraping = Button("Tweet scraper", 25)
        self.tweetScraping.clicked.connect(self.changeToScrape)
        self.tweetScraping.setToolTip("press me")

        self.retriveData = Button("Retrieve Data", 50)

        self.dataToGraph = Button("Data to graph", 25)
        self.dataToGraph.clicked.connect(self.changeToData)

        self.emailData = Button("Email Data", 25)
        self.emailData.clicked.connect(self.changeToEmail)

        self.settingsButton = Button("", 0)
        self.settingsButton.setIcon(QIcon("Computing project\Images\settings-icon-60.png")) ## This adds the icon of settings using the pyqt feuture QIcon
        self.settingsButton.setProperty("class", "settingsButtons") ## I then need to change the class of the button to settings class
        self.settingsButton.setIconSize(QSize(40, 40))
        self.settingsButton.setFixedSize(QSize(40, 40))
        self.settingsButton.setToolTip("Settings menue")
        self.settingsButton.clicked.connect(self.changeToSettings)

        self.exitButton = Button("", 0)
        self.exitButton.setIcon(QIcon("Computing project\Images\exit-icon.png"))
        self.exitButton.setProperty("class", "settingsButtons")
        self.exitButton.setIconSize(QSize(40, 40))
        self.exitButton.setFixedSize(QSize(40, 40))

        ## ADD WIDGETS TO LAYOUT ##
        self.mainVLayout.addLayout(self.topHLayout)
        self.topHLayout.addWidget(self.settingsButton, alignment=Qt.AlignmentFlag.AlignLeft)##add the widget to the top H layout
        self.topHLayout.addWidget(self.exitButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.mainVLayout.addWidget(self.centralTitle)##Adds the label to the layout at the postion (2)
        self.mainVLayout.addSpacing(8) ## adds a spacer between the button an  the title)
        ##This is where I attach all my buttons to the layout and then alignes them using the alingment flag tool
        self.mainVLayout.addWidget(self.tweetScraping, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.retriveData, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.dataToGraph, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainVLayout.addWidget(self.emailData, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.mainVLayout) ## This attaches the layout to this widget

        ## Ther first alignes the label to the top and the second centers the whole V layout.
        self.centralTitle.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainVLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def changeToSettings(self):
        from UI import changeSettings

        changeSettings()
        # with open(os.path.join(sys.path[0], "main style sheet.qss"), "r") as f:
        #         css = f.readlines()
        # print(css)
        # css[1] = ("    font-size: 12px;\n")
        # print(css)
        # with open(os.path.join(sys.path[0], "main style sheet.qss"), "w") as f:
        #     f.writelines(css)
        # from UI import settingsReset
        # settingsReset()

    def changeToScrape(self):
        from UI import changeScrape

        changeScrape()
    def changeToEmail(self):
        from UI import changeEmail

        changeEmail()
    def changeToData(self):
        from UI import changeData

        changeData()

    def changeFontTest(self):
        self.exitButton.setFont(QFont(40))
## The class which I use to create my buttons. Pyqt you have to do this with classes like if you were to do it in tkinter with functions
class Button(QPushButton):
    def __init__(self, parent=None, fontsize = 0): ##I need to know the name for button and what function it will call when clicked
        super().__init__(parent)
        
        self.setProperty("class", "menueButtons")##This aplies the class from my stylesheet to the widget
        self.setFont(QFont("Tahoma", fontsize)) ## Sets the font from the dictionary 
        self.setFixedSize(QSize(210, 58)) ## The set size of the button (widpth, hight)
        self.setChecked(True)