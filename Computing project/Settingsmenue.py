import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton) ##All the widgets I may use I'll import here


class SettingsMenue(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mainVLayout = QVBoxLayout()
        self.testButton = QPushButton("this is a test")
        self.testLabel = QLabel("this is a test")
        self.mainVLayout.addWidget(self.testLabel)
        self.mainVLayout.addWidget(self.testButton)
        
        self.setLayout(self.mainVLayout)
        


        

