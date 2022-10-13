import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton, QStackedWidget) ##All the widgets I may use I'll import here
from Settingsmenue import SettingsMenue 
from PrimaryMenue import PrimaryMenue


# class StackedWidgets(QStackedWidget):
#     def __init__(self):
#         QStackedWidget.__init__(self)

#         self.firstMenue = PrimaryMenue(self)
#         self.addWidget(self.firstMenue)
#         settingM = SettingsMenue(self)
#         self.addWidget(settingM)

#         ##This allows us to change the title of our window
#         self.setWindowTitle("Python Twitter scraper")##This is aimed at self(MainWindow)

#         #this determines the hieght and width of my program
#         self._height = 450 # change these if needed. currently there in the ratio 4:3 
#         self._length = 600
#         self.setFixedHeight(self._height)
#         self.setFixedWidth(self._length)

#         # #Orignally I would have used the font in my stylesheet but @font-faces does not work
#         # fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Arvo-Regular.ttf") ##This loads the font from the local location
#         # self.families = QFontDatabase.applicationFontFamilies(fontId) ## This allows me to have a dictionary of fonts
#         # fontId = QFontDatabase.addApplicationFont("Computing project\Fonts\Tahoma Regular font.ttf")

def changeSettings():
    global widgets
    settingM = SettingsMenue()
    widgets.addWidget(settingM)
    widgets.setCurrentIndex(1)



##creates the one application I'll use for my project
app = QApplication(sys.argv) ##An object which holds the event loop

widgets = QStackedWidget()
firstMenue = PrimaryMenue()
widgets.addWidget(firstMenue)
widgets.setFixedHeight(450)
widgets.setFixedWidth(600)

widgets.show()##All widgets need to be shown

## Opens the main style sheet for the project
with open(os.path.join(sys.path[0], "main style sheet.qss"), "r") as f: 
    _style = f.read() 
    app.setStyleSheet(_style)##Sets the style sheet

##Starts the loop
app.exec()

# if __name__ == '__main__': ##Starts the program
#     start()
