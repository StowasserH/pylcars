from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets


class Bracket(Widgets, QtWidgets.QPushButton):

    def __init__(self, lcars:QtWidgets.QWidget, rect: QtCore.QRect, text, color, style=None, svg=None):
        Widgets.__init__(self, lcars, svg)
        QtWidgets.QPushButton.__init__(self, lcars)
        self.setText(text)
        self.rect: QtCore.QRect = rect
        self.setFont(self.default_font)
        self.setFlat(True)
        self.setGeometry(rect)
        if not style:
            style = self.default_style
        self.style = style
        self.color = color
        self.paint_back(color=self.color)
        self.show()
