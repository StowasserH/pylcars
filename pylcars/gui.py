# -*- coding: utf-8 -*-
from PyQt4 import  QtCore, QtGui, QtSvg
import sys
import os


class Enumeration(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
    def __setattr__(self, name, value):
        raise RuntimeError("Cannot override values")
    def __delattr__(self, name):
        raise RuntimeError("Cannot delete values")
    class __metaclass__(type):
        def __iter__(self):
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item    

class Colors(Enumeration):
    orange = '#f90'
    flieder = '#c9c'
    blaugrau= '#99c'
    rostbraun= '#c66'
    beige= '#fc9'
    leuchtblau= '#99f'
    apricot= '#f96'
    pink= '#c69'
    hellorange= '#fc4'
    rot ='#c00'

class Conditions(Enumeration):
    alert =Colors.rot
    info  =Colors.beige
    use   =Colors.orange
    active=Colors.blaugrau
    
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class gui(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(_fromUtf8("border: none;\nbackground: #000;\n"))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.setupUi(self)
