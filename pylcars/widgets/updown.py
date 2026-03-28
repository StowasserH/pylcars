# -*- coding: utf-8 -*-
from typing import Optional
from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from .bracket import Bracket
from ..conditions import Conditions
from .semicircle import Semicircle
from ..orientation import Orientation


class Updown:
    sound_file: Optional[str]
    lcars: QtWidgets.QWidget
    color: str
    color_active: str
    text: str
    down: Semicircle
    up: Semicircle
    start: Bracket

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text: str = "text", color_use: str = Conditions.use,
                 color_active: str = Conditions.active, button_space: int = 4) -> None:
        self.sound_file = None
        self.lcars = lcars
        self.color = color_use
        self.color_active = color_active
        self.text = text
        rx = rect.x()
        ry = rect.y()
        rh = rect.height()
        rw = rect.width()
        self.down = Semicircle(lcars, QtCore.QRect(rx, ry, rh, rh)
                               , "< "
                               , self.color
                               , Orientation.left)

        self.up = Semicircle(lcars, QtCore.QRect(rx + rw - rh, ry, rh, rh)
                             , "> "
                             , self.color
                             , Orientation.right)

        self.start = Bracket(lcars, QtCore.QRect(rx + rh + button_space, ry, rw - 2 * (button_space + rh), rh)
                             , self.text
                             , self.color)

    def show(self) -> None:
        self.down.show()
        self.up.show()
        self.start.show()

    def hide(self) -> None:
        self.down.hide()
        self.up.hide()
        self.start.hide()
