"""Text label widget with LCARS styling.

This module implements the Textline widget, a text label with support for
custom colors, font sizes, and letter spacing for consistent LCARS typography.
"""
from typing import Optional, Union
from PyQt5 import QtCore, QtGui, QtWidgets

from pylcars import Deco


class Textline(Deco):
    """A text label widget with LCARS typography styling.

    A label widget designed for displaying text with LCARS font styling,
    custom colors, and adjustable font sizes. Supports dynamic color changes
    while maintaining consistent typography.

    Attributes:
        mainstyle: Base stylesheet used for the text element.
    """
    mainstyle: str

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text_color: str, text_height: Union[float, int], svg: Optional[str] = None, style: Optional[str] = None) -> None:
        """Initialize a Textline widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the text label.
            text_color: Color for the text.
            text_height: Font size in points.
            svg: Optional SVG template for background.
            style: Optional custom stylesheet base.
        """
        if not style:
            style = self.default_style
        self.mainstyle = style
        Deco.__init__(self, lcars, rect, text_color, svg, style + "color: " + text_color + ";")
        newfont = QtGui.QFont(self.default_font_name, text_height)
        newfont.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
        self.setFont(newfont)

    def change_color(self, color: str) -> None:
        """Change the text color while maintaining base styling.

        Args:
            color: New color for the text.
        """
        self.setStyleSheet(self.mainstyle + "color: " + color + ";")
