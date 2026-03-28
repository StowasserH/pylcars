from typing import Optional
from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets
import os


class Deco(Widgets, QtWidgets.QLabel):
    paint_pixmap: bool

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color: str, svg: Optional[str] = None, style: Optional[str] = None) -> None:
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

    def change_svg(self, svg: Optional[str]) -> None:
        self.svg = svg
        if self.svg is not None:
            url = self.build_svg(self.color)
            if url:
                self.paint_pixmap = True
                self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))

