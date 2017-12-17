from PyQt4 import QtCore, QtGui
from .widgets import Widgets


class Bracket(Widgets, QtGui.QPushButton):

    def __init__(self, lcars, rect, text, color, style=None):
        Widgets.__init__(self, lcars)
        QtGui.QPushButton.__init__(self, lcars)
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
