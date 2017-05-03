# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import (
    pyqtSignature,
    QObject,
    Qt,
    SIGNAL,
    QUrl,
    )

#from PyQt4 import QtCore

from PyQt4.QtGui import (
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QDialog,
    QFileDialog,
    QTextEdit,
    QColor,
    QAbstractItemView,
    )
from PyQt4 import QtCore
from Ui_mainWindow import Ui_MainWindow
from credits import DlgCredits
from util import doAlert



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def setupUi(self, mainWindow):
        super(MainWindow, self).setupUi(mainWindow)

    def __init__(self, parent=None, moses=None, workdir=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)

        css = QtCore.QFile('./gui/pyqt.css')
        css.open(QtCore.QIODevice.ReadOnly)
        if css.isOpen():
           self.setStyleSheet(QtCore.QVariant(css.readAll()).toString())
        css.close()




    @pyqtSignature("QString")
    def on_labelInfo_linkActivated(self, link):
        """
        Slot documentation goes here.
        """
        dialog = DlgCredits(self)
        dialog.exec_()
