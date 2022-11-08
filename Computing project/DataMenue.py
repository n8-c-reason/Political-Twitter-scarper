import sys ##Allows you to launch the app from commandline 
import os
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
     QHBoxLayout, QLabel, QGridLayout, QPushButton) ##All the widgets I may use I'll import here

class DataGraph(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mainVLayout = QVBoxLayout()
        self.backbutton = QPushButton()
        self.backbutton.setIcon(QIcon("Computing project\Images\icons8-go-back-90.png"))
        self.backbutton.setIconSize(QSize(40, 40))
        self.backbutton.setFixedSize(QSize(40, 40))
        self.backbutton.clicked.connect(self.back)

        self.testTitle = QLabel("Work in progress")
        self.mainVLayout.addWidget(self.testTitle)
    def back(self):
        from UI import backButton

        backButton()