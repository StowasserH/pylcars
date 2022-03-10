from PyQt5 import QtCore, QtGui

from pylcars import Deco

from .widgets import Widgets
import os


class Textline(Deco):
    def __init__(self, lcars, rect, text_color, svg=None, style=None):
        if not style:
            style = self.default_style
        self.mainstyle=style
        Deco.__init__(self, lcars, rect, text_color, svg, style + "color: " +  text_color + ";")

    def change_color(self,color):
        self.setStyleSheet(self.mainstyle + "color: " +  color + ";")