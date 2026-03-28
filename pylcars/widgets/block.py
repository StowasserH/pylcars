"""Block widget - a simple rectangular color block.

This module implements the Block widget, a decorative rectangular element
that renders as a solid colored rectangle using SVG.
"""
from typing import Optional
from PyQt5 import QtWidgets, QtCore

from .deco import Deco


class Block(Deco):
    """A rectangular block widget with a solid color.

    A decorative widget that displays as a simple colored rectangle.
    Used for creating visual separators, backgrounds, and color accents
    in the LCARS interface.

    Attributes:
        svg: SVG template for rendering a rectangle.
    """
    svg: str = '<svg height="{h}" width="{w}"><rect height="{h}" width="{w}" x="0" y="0" fill="{c}" /></svg>'

    def adapt_svg(self, color: Optional[str] = None) -> str:
        """Adapt SVG template with widget dimensions and color.

        Args:
            color: Color for the rectangle. If None, uses the widget's current color.

        Returns:
            Adapted SVG string with substituted dimensions and color.
        """
        h = self.rect.height()
        w = self.rect.width()
        c = color
        if not c:
            c = self.color
        return self.svg.format(h=h, w=w, c=c)

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, color: str, style: Optional[str] = None) -> None:
        """Initialize a Block widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the block.
            color: Color of the rectangular block.
            style: Optional custom stylesheet.
        """
        Deco.__init__(self, lcars, rect, color, style=style, svg=Block.svg)
