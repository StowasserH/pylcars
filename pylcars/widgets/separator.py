"""Separator widget for visual section division.

This module implements the Separator widget, which creates a decorative separator
element with a circular cap, bar, and optional second section based on orientation.
"""
from typing import Optional, Union
from PyQt5 import QtWidgets, QtCore

from .deco import Deco
from ..orientation import Orientation


class Separator(Deco):
    """A decorative separator widget with oriented elements.

    Creates a visual separator with a circular cap and rectangular bar.
    Can be oriented to point in different directions (top, bottom, left, right)
    and is commonly used to divide interface sections.

    Attributes:
        svg: SVG template for rendering the separator.
        bar_width: Width of the bar section.
        orientation: Direction the separator points (from Orientation enum).
    """
    svg: str = '<svg height="{h}" width="{w}">' \
          '<circle cx="{h2}" cy="{h2}" r="{h2}" fill="{c}" />' \
          '<rect height="{h2}" width="{bar}" x="0" y="{h0}" fill="{c}" />' \
          '<rect height="{h2}" width="{w}" x="{h2}" y="{hm}" fill="{c}" />' \
          '<circle cx="{bar}" cy="{htot}" r="{h2}" fill="#000" />' \
          '</svg>'
    bar_width: Union[float, int]
    orientation: int

    def adapt_svg(self, color: Optional[str] = None) -> str:
        """Adapt SVG template based on orientation and dimensions.

        Args:
            color: Color for the separator. If None, uses widget's current color.

        Returns:
            Adapted SVG string with orientation-specific values substituted.
        """
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

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color: str, bar_width: Union[float, int], style: Optional[str] = None,
                 orientation: int = Orientation.top, svg: Optional[str] = None) -> None:
        """Initialize a Separator widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the separator.
            color: Color of the separator.
            bar_width: Width of the bar section.
            style: Optional custom stylesheet.
            orientation: Direction the separator points (default: Orientation.top).
            svg: Optional custom SVG template.
        """
        if svg is None:
            svg = Separator.svg
        self.bar_width = bar_width + (rect.height() / 2)
        self.orientation = orientation
        Deco.__init__(self, lcars, rect, color, style=style, svg=svg)
