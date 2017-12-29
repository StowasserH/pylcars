# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, QtSvg
from .separator import Separator
from ..conditions import Conditions
from ..orientation import Orientation
from .bracket import Bracket
from .block import Block
from functools import partial


class Menue():
    def menu_click(self, button_name="\n"):
        if not self.enabled:
            return
        if self.active_page != button_name:
            self.lcars.play_sound()
            self.blend_out(self.active_page)
            self.buttons[self.active_page].tockle()
            self.active_page = button_name
            self.buttons[self.active_page].tockle(self.color_active)
            self.blend_in(self.active_page)

    def blend_out(self, page):
        widgets = self.pages[page]
        for widget in widgets:
            widgets[widget].hide()

    def blend_in(self, page):
        widgets = self.pages[page]
        for widget in widgets:
            widgets[widget].show()

    def paint_back(self, color):
        for button in self.fields:
            self.buttons[button].paint_back(color)
        self.top.paint_back(color)
        self.bot.paint_back(color)
        self.linetop.paint_back(color)
        self.linebot.paint_back(color)
        self.fill.paint_back(color)

    def setEnabled(self,enabled):
        self.enabled = enabled

    def __init__(self, lcars, fields, rect, button_size, color_use=Conditions.use, color_active=Conditions.active,
                 button_space=4, button_callback=None):
        self.lcars = lcars
        self.color = color_use
        self.color_active = color_active
        self.enabled = True
        rx = rect.x()
        ry = rect.y()
        rh = rect.height()
        rw = rect.width()
        bw = button_size.width()
        bh = button_size.height()
        seperator_width = bw + bw / 2
        self.top = Separator(lcars, QtCore.QRect(rx, ry, seperator_width, bh), color_use, bw,
                             orientation=Orientation.top)
        self.buttons = {}
        self.pages = {}
        self.fields = fields
        pos = bh + button_space
        self.button_callback = button_callback if button_callback else self.menu_click
        for button in self.fields:
            self.buttons[button] = Bracket(lcars, QtCore.QRect(rx, pos, bw, bh), button + " ", color_use)
            self.buttons[button].clicked.connect(partial(self.button_callback, button_name=button))
            pos += bh + button_space
            self.pages[button] = {}
        self.active_page = fields[0]
        self.buttons[self.active_page].tockle(Conditions.active)
        self.bot = Separator(lcars, QtCore.QRect(rx, rh - bh, seperator_width, bh), color_use, bw,
                             orientation=Orientation.bottom)
        lx = rx + seperator_width + button_space
        lw = rw - lx

        self.linetop = Block(lcars, QtCore.QRect(lx, ry, lw, bh / 2), Conditions.use)
        bs = rh - bh / 2
        self.linebot = Block(lcars, QtCore.QRect(lx, bs, lw, bh / 2), Conditions.use)
        # pos += bh + button_space
        self.fill = Block(lcars, QtCore.QRect(rx, pos, bw, rh - bh - pos - button_space), Conditions.use)
