from PyQt5 import QtCore, QtGui, QtWidgets

from pylcars import Deco


class Textline(Deco):
    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text_color, text_height, svg=None, style=None):
        if not style:
            style = self.default_style
        self.mainstyle = style
        Deco.__init__(self, lcars, rect, text_color, svg, style + "color: " + text_color + ";")
        newfont = QtGui.QFont(self.default_font_name, text_height)
        newfont.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
        self.setFont(newfont)

    def change_color(self, color):
        self.setStyleSheet(self.mainstyle + "color: " + color + ";")
