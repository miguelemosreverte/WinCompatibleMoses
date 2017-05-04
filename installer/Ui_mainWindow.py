# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\work\eric4workspace\MosesGUI\mainWindow.ui'
#
# Created: Thu Jul 11 13:38:46 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtSvg

import sys,os
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import time
import icons_rc
_fromUtf8 = getattr(QtCore.QString, 'fromUtf8', lambda s: s)


def _translate(context, text, disambig):
    return QtGui.QApplication.translate(
        context, text, disambig,
        getattr(
            QtGui.QApplication, 'UnicodeUTF8',
            QtCore.QCoreApplication.Encoding))
class MyCustomWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)
        layout = QtGui.QVBoxLayout(self)

        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setRange(0,100)
        self.progressBar.setValue(0 + os.path.isfile("current.txt") * 20)
        self.button = QtGui.QPushButton("Continue" if os.path.isfile("current.txt") else "Start", self)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.onStart)

        self.myLongTask = TaskThread()
        self.mySecondLongestLongTask = FakeProgress()
        self.mySecondLongestLongTask.notifyProgress.connect(self.onProgress)


    def onStart(self):
        self.mySecondLongestLongTask.start()
        self.myLongTask.start()
        self.button.setEnabled(False)

    def onProgress(self, i):
        self.progressBar.setValue(i)


class FakeProgress(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(int)
    def run(self):
        for i in range(1,100):#this will take roughly 4 hours
            self.notifyProgress.emit(i)
            time.sleep((4*60*60)/100)

class TaskThread(QtCore.QThread):
    def run(self):
        if not os.path.isfile("current.txt"):
            os.system("python step_one.py")
        else:
            os.system("python step_two.py")

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(705, 491)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/moses.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))


        groupBox= QtGui.QGroupBox()
        groupBox.setObjectName(_fromUtf8("groupBox"))
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))
        groupBox.setStyleSheet("border-image: url(docker.png);")

        self.progressBar = MyCustomWidget(self.centralWidget)

        verticalLayout.addWidget(groupBox)
        verticalLayout.addWidget(self.progressBar)


        self.labelInfo = QtGui.QLabel(self.centralWidget)
        self.labelInfo.setTextFormat(QtCore.Qt.AutoText)
        self.labelInfo.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter)
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        label_texts = ["Warning: This could take up to 4 hours, and there's a reboot incoming", 
                       "Okay, no more reboots. Just hours of slow install. You can sit back and enjoy now."]
        self.labelInfo.setText(label_texts[os.path.isfile("current.txt")])
        verticalLayout.addWidget(self.labelInfo)
        MainWindow.setCentralWidget(self.centralWidget)

        MainWindow.setWindowTitle(_translate("MainWindow", "Dockerizing Moses in Windows", None))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
