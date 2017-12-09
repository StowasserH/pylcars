# -*- coding: utf-8 -*-
from PyQt4 import  QtCore, QtGui, QtSvg
import sys
import os
import xxhash
import os.path

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


class Gui(QtGui.QMainWindow):
   
    def setDefaultFont(self,fontName,size=26):
        self.defaultFont=QtGui.QFont()
        self.defaultFont.setFamily(self.defaultFontName)
        self.defaultFont.setPointSize(size)
        self.defaultFont.setStrikeOut(False)

    def renderSvg(self,svg,size):
        renderer = QtSvg.QSvgRenderer(QtCore.QByteArray(svg))
        qim = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        qim.fill(0)
        painter = QtGui.QPainter()
        painter.begin(qim)
        renderer.render(painter)
        painter.end()
        return qim
    
    def saveImg(self,svg,size):
        name=xxhash.xxh64(svg+str(size)).hexdigest()
        path=os.path.join(self.imageFolder, name[:3],name[3:6])
        filename=name[6:]+".png"
        url=os.path.join(path,filename)
        if not os.path.isfile(url):
            if not os.path.isdir(path):
                os.makedirs(path)
            image=self.renderSvg(svg,size)
            image.save(url,"PNG")
        return url
    
    def createButton(self,svg,size,text):
        button = QtGui.QPushButton(self.centralwidget)
        button.setFont(self.defaultFont)
        url=self.saveImg(svg,size)
        button.setStyleSheet( self.defaultStyle+"\nbackground-image: url("+url+");" )
        button.setText(_translate("MainWindow", text, None))
        button.setFlat(True)
        return button
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(self.mainWindowSize)
        MainWindow.setStyleSheet(self.defaultStyle)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        #self.defaultStyle=_fromUtf8("border: none;\nbackground: #000;\n")
        #"background-image: url(:/AddButton.png);"
        #"background-repeat: no-repeat;"
        #"background-position: center center"
        self.defaultStyle=_fromUtf8("border: none;\nbackground: #000;\nText-align: right;")
        self.defaultFontName=_fromUtf8("LCARS")
        self.setDefaultFont(self.defaultFontName)
        self.imageFolder="background"
        self.mainWindowSize=QtCore.QSize(800, 480)
        self.setupUi(self)
