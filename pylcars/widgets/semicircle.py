from PyQt4 import QtCore,QtGui
from pylcars.orientation import Orientation
from .widgets import Widgets


class Semicircle(Widgets, QtGui.QPushButton):

    svg = ('<svg height="{h}" width="{w}">'
               '<circle cx="{r}" cy="{r}" r="{r}" fill="{c}" />'
               '<rect height="{rh}" width="{rw}" x="{rx}" y="{ry}" fill="{c}" />'
               '</svg>')

    default_style = "border: none;\nbackground: #000;\nText-align: right;"

    def adapt_svg(self):
        rect=self.geometry()
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
        return self.svg.format(h=h, w=w,
                                  r=r,
                                  rh=rh, rw=rw, rx=rx, ry=ry,
                                  c=self.color)


    def blank(self, rect, text, color):
        style = "border: none;\nbackground: " + color + ";\nText-align: right;"
        button = self.createButton(QtCore.QSize(rect.width(), rect.height()), text, style=style)
        button.setGeometry(rect)
        return button

    def __init__(self,lcars, rect, text,color,orientation,style=None):
        Widgets.__init__(self,lcars)
        QtGui.QPushButton.__init__(self,lcars)
        #self.default_style = "border: none;\nbackground: #000;\nText-align: right;"
        self.setText(text)
        self.setFont(self.default_font)
        self.setFlat(True)
        self.setGeometry(rect)
        if not style:
            style = self.default_style
        self.orientation = orientation
        self.color = color
        svg = self.adapt_svg()
        url = self.save_img(svg, QtCore.QSize(rect.width(),rect.height()))
        style += "\nbackground-image: url(" + url + ");"
        self.setStyleSheet(style)
        self.show()
        #button.setText(_translate("MainWindow", text, None))
