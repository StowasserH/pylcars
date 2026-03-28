from typing import Optional, Union
from PyQt5 import QtCore, QtGui, QtWidgets

from pylcars import Deco


class Textline(Deco):
    mainstyle: str

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text_color: str, text_height: Union[float, int], svg: Optional[str] = None, style: Optional[str] = None) -> None:
        if not style:
            style = self.default_style
        self.mainstyle = style
        Deco.__init__(self, lcars, rect, text_color, svg, style + "color: " + text_color + ";")
        newfont = QtGui.QFont(self.default_font_name, text_height)
        newfont.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
        self.setFont(newfont)

    def change_color(self, color: str) -> None:
        self.setStyleSheet(self.mainstyle + "color: " + color + ";")
