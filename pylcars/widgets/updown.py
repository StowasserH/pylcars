# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtSvg
from .bracket import Bracket
from ..conditions import Conditions
from .semicircle import Semicircle
from ..orientation import Orientation


class Updown:
    def __init__(self, lcars, rect,text="text", color_use=Conditions.use, color_active=Conditions.active, button_space=4):
        self.sound_file = None
        self.lcars = lcars
        self.color = color_use
        self.color_active = color_active
        self.text=text
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

    def show(self):
        self.down.show()
        self.up.show()
        self.start.show()

    def hide(self):
        self.down.hide()
        self.up.hide()
        self.start.hide()