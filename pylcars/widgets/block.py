from PyQt5 import QtWidgets, QtCore

from .deco import Deco


class Block(Deco):
    svg = '<svg height="{h}" width="{w}"><rect height="{h}" width="{w}" x="0" y="0" fill="{c}" /></svg>'

    def adapt_svg(self, color=None):
        h = self.rect.height()
        w = self.rect.width()
        c = color
        if not c:
            c = self.color
        return self.svg.format(h=h, w=w, c=c)

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color, style=None):
        Deco.__init__(self,lcars, rect, color, style=style, svg=Block.svg)
