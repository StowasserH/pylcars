# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtSvg
import os
import xxhash
import os.path


class Widgets:
    default_style = "border: none;\nbackground: {bg};\nText-align: right;"

    def __init__(self, lcars):
        self.toggle = False
        self.lcars = lcars
        self.default_font = QtGui.QFont()
        self.default_font_name = "LCARS"
        self.set_default_font()
        self.image_folder = "background"
        self.background_col = "#000"

    def tickle(self, color):
        self.paint_back(color)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.tickle_done)
        timer.setSingleShot(True)
        timer.start(300)

    def tickle_done(self):
        self.paint_back(self.color)

    def tockle(self, color=None):
        if not self.toggle and color:
            self.paint_back(color)
        else:
            self.paint_back(self.color)
        self.toggle=not self.toggle

    def set_default_font(self, fontname=None, size=26):
        if not fontname:
            fontname = self.default_font_name
        self.default_font.setFamily(fontname)
        self.default_font.setPointSize(size)
        self.default_font.setStrikeOut(False)

    def adapt_svg(self, color=None):
        rect = self.rect
        h = rect.height()
        w = rect.width()
        c = color
        if not c:
            c = self.color
        return self.svg.format(h=h, w=w, c=c)

    def build_svg(self, color=None):
        svg = self.adapt_svg(color)
        return self.save_img(svg, QtCore.QSize(self.rect.width(), self.rect.height()))

    def parse_style(self, style, bgcol=None):
        if not bgcol:
            bgcol = self.background_col
        return style.format(bg=bgcol)

    def paint_back(self, color=None):
        if hasattr(self, 'svg'):
            url=self.build_svg(color)
            if hasattr(self, 'paint_pixmap'):
                self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))
            style = self.parse_style(self.style, bgcol=self.background_col)
            self.setStyleSheet(style + "\nbackground-image: url(" + url + ");")
        else:
            style = self.parse_style(self.style, bgcol=color)
            self.setStyleSheet(style)

    def render_svg(self, svg, size):
        qByteArray = QtCore.QByteArray()
        qByteArray.append(svg)
        renderer = QtSvg.QSvgRenderer(qByteArray)
        qim = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        qim.fill(0)
        painter = QtGui.QPainter()
        painter.begin(qim)
        renderer.render(painter)
        painter.end()
        return qim

    def save_img(self, svg, size):
        name = xxhash.xxh64(svg + str(size)).hexdigest()
        path = os.path.join(self.image_folder, name[:3], name[3:6])
        filename = name[6:] + ".png"
        url = os.path.join(path, filename)
        if not os.path.isfile(url):
            if not os.path.isdir(path):
                os.makedirs(path)
            image = self.render_svg(svg, size)
            image.save(url, "PNG")
        return url
