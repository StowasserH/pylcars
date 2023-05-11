from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets
import os


class Deco(Widgets, QtWidgets.QLabel):
    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color, svg=None, style=None):
        self.paint_pixmap = False
        if not style:
            style = self.default_style
        self.style = style
        Widgets.__init__(self, lcars, svg)
        QtWidgets.QLabel.__init__(self, lcars)
        self.setGeometry(rect)
        self.setFont(self.default_font)
        self.color = color
        self.rect: QtCore.QRect = rect
        self.change_svg(self.svg)
        self.setStyleSheet(self.style)
        self.show()

    def change_svg(self, svg: str):
        print (svg)
        self.svg = svg
        if self.svg is not None:
            url = self.build_svg(self.color)
            if url:
                print(url)
                self.paint_pixmap = True
                self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))

