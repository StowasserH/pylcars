# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui,QtSvg
import os
import xxhash
import os.path



class Widgets:
    def __init__(self, lcars):
        self.lcars = lcars
        self.default_font = QtGui.QFont()
        self.default_font_name = "LCARS"
        self.set_default_font()
        self.image_folder = "background"

    def set_default_font(self, fontname=None, size=26):
        if not fontname:
            fontname = self.default_font_name
        print "font=" + fontname
        self.default_font.setFamily(fontname)
        self.default_font.setPointSize(size)
        self.default_font.setStrikeOut(False)

    def render_svg(self, svg, size):
        renderer = QtSvg.QSvgRenderer(QtCore.QByteArray(svg))
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


