# -*- coding: utf-8 -*-

import sys,os

from PyQt4.QtGui import (
    QApplication,
    QMessageBox,
    )


def doAlert(text):
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.setWindowTitle("Message")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.exec_()


def doQuestion(text):
    reply = QMessageBox.question(
        None, 'Message', text, QMessageBox.Yes, QMessageBox.No)
    if reply == QMessageBox.Yes:
        return True
    else:
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if doQuestion("Reboot now"): 
        os.system("shutdown -r -t 0")
