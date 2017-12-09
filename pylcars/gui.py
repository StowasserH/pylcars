# -*- coding: utf-8 -*-
from PyQt4 import  QtCore, QtGui, QtSvg
import sys
import os
import xxhash
import os.path


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
    #def defaultStyle
    #def defaultFontName
    #def defaultFont
    
    def setDefaultFont(self,fontName,size=26):
        self.defaultFont=QtGui.QFont()
        self.defaultFont.setFamily(self.defaultFontName)
        self.defaultFont.setPointSize(size)
        self.defaultFont.setStrikeOut(False)

    def renderSvg(self,svg,size):
        if (type(size) is not QtCore.QSize):
            raise AttributeError("Pass QSize")
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
        path=self.imageFolder + os.sep + name[:3]+ os.sep + name[3:6]+ os.sep 
        filename=name[6:]+".png"
        url=path+filename
        if(not os.path.isfile(url)):
          if( not os.path.isdir(path)):
            os.makedirs(path)
          image=self.renderSvg(svg,size)
          image.save(url,"PNG")
        return url
    
    def createButton(self,svg,size,text):
        if (type(size) is not QtCore.QSize):
            raise AttributeError("Pass QSize")
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
        super(gui, self).__init__(parent)
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
