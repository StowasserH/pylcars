from PyQt4 import QtCore, QtGui
from pylcars.orientation import Orientation
from .widgets import Widgets
from .bracket import Bracket

class Semicircle(Bracket):
    svg = ('<svg height="{h}" width="{w}">'
           '<circle cx="{r}" cy="{r}" r="{r}" fill="{c}" />'
           '<rect height="{rh}" width="{rw}" x="{rx}" y="{ry}" fill="{c}" />'
           '</svg>')

    def adapt_svg(self, color=None):
        rect = self.geometry()
        rh = h = rect.height()
        rw = w = rect.width()
        rx = ry = 0
        r = h / 2
        if self.orientation == Orientation.left:
            rx = r
        elif self.orientation == Orientation.right:
            rw = r
        elif self.orientation == Orientation.top:
            rh = r
        elif self.orientation == Orientation.bottom:
            ry = r
        c = color
        if not c:
            c = self.color
        return self.svg.format(h=h, w=w,r=r,rh=rh, rw=rw, rx=rx, ry=ry,c=c)

    def __init__(self, lcars, rect, text, color, orientation, style=None):
        self.orientation = orientation
        Bracket.__init__(self, lcars, rect, text, color, style)
