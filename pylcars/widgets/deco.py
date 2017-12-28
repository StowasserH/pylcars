from PyQt4 import QtCore, QtGui
from .widgets import Widgets
import os


class Deco(Widgets, QtGui.QLabel):
    def __init__(self, lcars, rect, color, svg=None, style=None):
        Widgets.__init__(self, lcars)
        QtGui.QLabel.__init__(self, lcars)
        self.setGeometry(rect)
        self.setFont(self.default_font)
        if svg:
            self.svg = svg
        self.rect = rect
        self.color = color
        if not style:
            style = self.default_style
        self.style = style
        if hasattr(self, 'svg'):
            url = self.build_svg(color)
            self.paint_pixmap = True
            self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))
        self.show()
