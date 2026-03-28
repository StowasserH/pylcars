"""Decorative widget base class with SVG and pixmap support.

This module implements the Deco widget class, which extends Widgets with
QLabel functionality for rendering SVG-based graphics and pixmaps.
"""
from typing import Optional
from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets
import os


class Deco(Widgets, QtWidgets.QLabel):
    """A decorative label widget with SVG rendering support.

    A label widget that extends the base Widgets class with QLabel functionality,
    allowing rendering of both SVG graphics and traditional pixmap images.
    Primarily used for non-interactive visual elements in the interface.

    Attributes:
        paint_pixmap: Flag indicating whether a pixmap background is being used.
    """
    paint_pixmap: bool

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color: str, svg: Optional[str] = None, style: Optional[str] = None) -> None:
        """Initialize a Deco widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the widget.
            color: Primary color for the widget.
            svg: Optional SVG template for rendering.
            style: Optional custom stylesheet.
        """
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
        """Change the SVG template and render the widget.

        Updates the widget's SVG template and renders it as a pixmap.
        If SVG is None, the widget is updated but no pixmap is set.

        Args:
            svg: New SVG template string, or None to disable SVG rendering.
        """
        self.svg = svg
        if self.svg is not None:
            url = self.build_svg(self.color)
            if url:
                self.paint_pixmap = True
                self.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), url)))

