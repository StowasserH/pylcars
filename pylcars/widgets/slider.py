"""Slider widget with LCARS styling.

This module implements the Slider widget, a customizable slider control
with support for both horizontal and vertical orientations, using LCARS colors
and styling for visual consistency.
"""
from typing import Optional
from PyQt5 import QtCore, QtGui, QtWidgets

from .widgets import Widgets
from .. import Colors


class Slider(Widgets, QtWidgets.QSlider):
    """A styled slider control for LCARS interface.

    A slider widget that combines QSlider functionality with LCARS styling.
    Supports both horizontal and vertical orientations with customizable colors
    for the groove, handle, and border.

    Attributes:
        default_style: Stylesheet template for the slider with color placeholders.
    """
    default_style: str = """  QSlider::groove:horizontal {{
                            border: 2px solid;
                            height: 10px;
                            background-color: {col1:s};
                            margin: 2px 0;
                            }}
                        QSlider::handle:horizontal {{
                            background-color: {col3:s};
                            border: 2px solid;
                            height: {height:d}px;
                            width: {width:d}px;
                            margin: -15px 0px;
                            border-radius: 6px;
                            border-color: {col2:s};;
                            }}
                        QSlider::groove:vertical {{
                            border: 2px solid;
                            width: 10px;
                            background-color: {col1:s};
                            margin: 0 2px;
                            }}
                        QSlider::handle:vertical {{
                            background-color: {col3:s};
                            border: 2px solid;
                            height: {height:d}px;
                            width: {width:d}px;
                            margin: 0px -15px;
                            border-radius: 6px;
                            border-color: {col2:s};;
                            }}
                        """

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, orientation: int = QtCore.Qt.Horizontal,
                 color1: str = Colors.orange, color2: str = Colors.flieder, color3: str = Colors.orange,
                 style: Optional[str] = None) -> None:
        """Initialize a Slider widget.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the slider.
            orientation: Slider orientation (default: QtCore.Qt.Horizontal).
            color1: Color for the groove (default: Colors.orange).
            color2: Color for the border (default: Colors.flieder).
            color3: Color for the handle (default: Colors.orange).
            style: Optional custom stylesheet. If not provided, uses default_style.
        """
        Widgets.__init__(self, lcars)
        QtWidgets.QSlider.__init__(self, lcars)
        # self.setText(text)
        self.rect: QtCore.QRect = rect
        self.setOrientation(orientation)
        # self.setFont(self.default_font)
        # self.setFlat(True)
        self.setGeometry(rect)
        if not style:
            if orientation == QtCore.Qt.Horizontal:
                style = self.default_style.format(width=int(rect.height() / 2), height=rect.height(),
                                                  col1=color1, col2=color2, col3=color3)
            else:
                style = self.default_style.format(width=rect.width(), height=int(rect.width() / 2),
                                                  col1=color1, col2=color2, col3=color3)
        # self.style = style
        self.setStyleSheet(style)
        # self.color = color
        # self.paint_back(color=self.color)
        self.show()
