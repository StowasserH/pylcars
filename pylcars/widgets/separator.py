from PyQt5 import QtWidgets, QtCore

from .deco import Deco
from ..orientation import Orientation


class Separator(Deco):
    svg = '<svg height="{h}" width="{w}">' \
          '<circle cx="{h2}" cy="{h2}" r="{h2}" fill="{c}" />' \
          '<rect height="{h2}" width="{bar}" x="0" y="{h0}" fill="{c}" />' \
          '<rect height="{h2}" width="{w}" x="{h2}" y="{hm}" fill="{c}" />' \
          '<circle cx="{bar}" cy="{htot}" r="{h2}" fill="#000" />' \
          '</svg>'

    def adapt_svg(self, color=None):
        rect = self.rect
        h = rect.height()
        w = rect.width()
        c = color
        if not c:
            c = self.color
        if self.orientation == Orientation.bottom:
            h0 = 0
            hm = h / 2
            htot = 0
        else:
            h0 = h / 2
            hm = 0
            htot = h
        return self.svg.format(h=h, w=w, c=c, h2=h / 2, h0=h0, htot=htot, hm=hm, bar=self.bar_width)

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color, bar_width, style=None,
                 orientation=Orientation.top, svg=None):
        if svg is None:
            svg = Separator.svg
        self.bar_width = bar_width + (rect.height() / 2)
        self.orientation = orientation
        Deco.__init__(self, lcars, rect, color, style=style, svg=svg)
