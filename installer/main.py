# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication

import os,sys

from mainWindow import MainWindow

if __name__ == "__main__":

    absFilePath = os.path.abspath(__file__)
    os.chdir( os.path.dirname(absFilePath) )
    
    app = QApplication(sys.argv)

    MainWindow = MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
