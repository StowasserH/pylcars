"""Semicircle button widget for directional navigation.

This module implements the Semicircle widget, a button with a semicircular
cap that points in a specific direction, commonly used for navigation arrows.
"""
from typing import Optional, Union
from PyQt5 import QtWidgets, QtCore

from pylcars.orientation import Orientation
from .bracket import Bracket


class Semicircle(Bracket):
    """A semicircular button widget pointing in a cardinal direction.

    A button widget shaped like a semicircle with a rectangular bar, pointing
    in one of four cardinal directions (up, down, left, right). Commonly used
    for directional navigation in menus.

    Attributes:
        svg: SVG template for rendering the semicircle shape.
        orientation: Direction the semicircle points (from Orientation enum).
    """
    svg: str = ('<svg height="{h}" width="{w}">'
           '<circle cx="{r}" cy="{r}" r="{r}" fill="{c}" />'
           '<rect height="{rh}" width="{rw}" x="{rx}" y="{ry}" fill="{c}" />'
           '</svg>')
    orientation: int

    def adapt_svg(self, color: Optional[str] = None) -> str:
        """Adapt SVG template based on orientation and dimensions.

        Args:
            color: Color for the semicircle. If None, uses widget's current color.

        Returns:
            Adapted SVG string with orientation-specific values substituted.
        """
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
        return self.svg.format(h=h, w=w, r=r, rh=rh, rw=rw, rx=rx, ry=ry, c=c)

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text: str, color: str, orientation: int, style: Optional[str] = None) -> None:
        """Initialize a Semicircle button widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the button.
            text: Button label text.
            color: Background color for the button.
            orientation: Direction the semicircle points (from Orientation enum).
            style: Optional custom stylesheet.
        """
        self.orientation = orientation
        Bracket.__init__(self, lcars, rect, text, color, style, svg=Semicircle.svg)
