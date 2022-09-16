import sys ##Allows you to launch the app from commandline 
from PyQt6.QtWidgets import (QMainWindow, QApplication) ##All the widgets I may use I'll import here


if __name__ == '__main__': ##Starts the program

    ##creates the one application I'll use for my project
    app = QApplication(sys.argv) ##An object which holds the event loop

    ##Creates my first  top level widget widnow
    main_menue = QMainWindow() ## In this case it is QMainWindow

    main_menue.show() ##All widgets need to be shown

    ##Starts the loop
    app.exec()
