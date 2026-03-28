"""Bracket button widget for LCARS interface.

This module implements the bracket button widget, a rectangular button with
customizable color, text, and optional SVG-based background rendering.
"""
from typing import Optional
from PyQt5 import QtCore, QtGui, QtWidgets
from .widgets import Widgets


class Bracket(Widgets, QtWidgets.QPushButton):
    """A rectangular button widget with LCARS styling.

    A push button widget that combines QPushButton functionality with LCARS
    styling, color theming, and optional SVG background rendering. Can be
    used for navigation, commands, and other interactive elements.

    Attributes:
        rect: Geometry rectangle of the button.
        style: Stylesheet for the button.
        color: Color of the button background.
    """

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text: str, color: str, style: Optional[str] = None, svg: Optional[str] = None) -> None:
        """Initialize a Bracket button widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the button.
            text: Button label text.
            color: Background color for the button.
            style: Optional custom stylesheet. Uses default if not provided.
            svg: Optional SVG template for custom background rendering.
        """
        Widgets.__init__(self, lcars, svg)
        QtWidgets.QPushButton.__init__(self, lcars)
        self.setText(text)
        self.rect: QtCore.QRect = rect
        self.setFont(self.default_font)
        self.setFlat(True)
        self.setGeometry(rect)
        if not style:
            style = self.default_style
        self.style = style
        self.color = color
        self.paint_back(color=self.color)
        self.show()
