from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets


class Bracket(Widgets, QtWidgets.QPushButton):

    def __init__(self, lcars, rect, text, color, style=None):
        Widgets.__init__(self, lcars)
        QtWidgets.QPushButton.__init__(self, lcars)
        self.setText(text)
        self.rect = rect
        self.setFont(self.default_font)
        self.setFlat(True)
        self.setGeometry(rect)
        if not style:
            style = self.default_style
        self.style = style
        self.color = color
        self.paint_back(color=self.color)
        self.show()
