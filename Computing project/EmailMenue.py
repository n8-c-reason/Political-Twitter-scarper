import sys ##Allows you to launch the app from commandline 

from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton) ##All the widgets I may use I'll import here

class EmailData(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mainVLayout = QVBoxLayout()
        ##Back button
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backButton.setIconSize(QSize(40, 40))
        self.backButton.setFixedSize(QSize(40, 40))
        self.backButton.clicked.connect(self.back)
        ##Work in progress label
        self.testTitle = QLabel("Work in progress")
        self.mainVLayout.addWidget(self.backButton)
        self.mainVLayout.addWidget(self.testTitle)
        self.setLayout(self.mainVLayout)
    
    ##takes back to main menu
    def back(self):
        from UI import backButton

        backButton()