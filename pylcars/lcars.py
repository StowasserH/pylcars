# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from .sound import Sound

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Lcars(Sound, QtWidgets.QMainWindow):
    default_style = "border: none;\nbackground: #000;\n"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(self.mainWindowSize)
        MainWindow.setStyleSheet(self.default_style)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        Sound.__init__(self)
        # self.defaultStyle=_fromUtf8("border: none;\nbackground: #000;\n")
        # "background-image: url(:/AddButton.png);"
        # "background-repeat: no-repeat;"
        # "background-position: center center"

        self.mainWindowSize = QtCore.QSize(800, 480)
        self.setupUi(self)
