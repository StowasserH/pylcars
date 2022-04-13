from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets
import os


class Deco(Widgets, QtWidgets.QLabel):
    def __init__(self, lcars:QtWidgets.QWidget, rect: QtCore.QRect, color, svg=None, style=None):
        if not style:
            style = self.default_style
        self.style = style
        Widgets.__init__(self, lcars)
        QtWidgets.QLabel.__init__(self, lcars)
        self.setGeometry(rect)
        self.setFont(self.default_font)
        if svg:
            self.svg = svg
        self.rect: QtCore.QRect = rect
        self.color = color
        if hasattr(self, 'svg'):
            url = self.build_svg(color)
            self.paint_pixmap = True
            self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))
        self.setStyleSheet(self.style)
        self.show()
