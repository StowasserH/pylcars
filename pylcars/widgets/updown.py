# -*- coding: utf-8 -*-
"""Up/Down navigation control widget.

This module implements the Updown widget, a composite control with up and down
navigation buttons flanking a central button, commonly used for menu navigation.
"""
from typing import Optional
from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from .bracket import Bracket
from ..conditions import Conditions
from .semicircle import Semicircle
from ..orientation import Orientation


class Updown:
    """A navigation control with up/down buttons and central button.

    Composite widget consisting of two semicircle buttons (up/down arrows) with
    a central bracket button. Commonly used for navigating through menu options
    or incrementing/decrementing values.

    Attributes:
        sound_file: Optional path to sound file to play on interaction.
        lcars: Reference to parent LCARS window.
        color: Primary color for the control.
        color_active: Color when active/selected.
        text: Label text for the central button.
        down: Down navigation semicircle button.
        up: Up navigation semicircle button.
        start: Central bracket button.
    """
    sound_file: Optional[str]
    lcars: QtWidgets.QWidget
    color: str
    color_active: str
    text: str
    down: Semicircle
    up: Semicircle
    start: Bracket

    def __init__(self, lcars: QtWidgets.QWidget, rect: QtCore.QRect, text: str = "text", color_use: str = Conditions.use,
                 color_active: str = Conditions.active, button_space: int = 4) -> None:
        """Initialize an Updown navigation control.

        Args:
            lcars: Parent LCARS window.
            rect: Geometry rectangle for the entire control.
            text: Label text for the central button (default: "text").
            color_use: Color for the control in normal state (default: Conditions.use).
            color_active: Color for the control when active (default: Conditions.active).
            button_space: Spacing between buttons in pixels (default: 4).
        """
        self.sound_file = None
        self.lcars = lcars
        self.color = color_use
        self.color_active = color_active
        self.text = text
        rx = rect.x()
        ry = rect.y()
        rh = rect.height()
        rw = rect.width()
        self.down = Semicircle(lcars, QtCore.QRect(rx, ry, rh, rh)
                               , "< "
                               , self.color
                               , Orientation.left)

        self.up = Semicircle(lcars, QtCore.QRect(rx + rw - rh, ry, rh, rh)
                             , "> "
                             , self.color
                             , Orientation.right)

        self.start = Bracket(lcars, QtCore.QRect(rx + rh + button_space, ry, rw - 2 * (button_space + rh), rh)
                             , self.text
                             , self.color)

    def show(self) -> None:
        """Show all components of the control.

        Makes the up button, down button, and central button visible.
        """
        self.down.show()
        self.up.show()
        self.start.show()

    def hide(self) -> None:
        """Hide all components of the control.

        Makes the up button, down button, and central button invisible.
        """
        self.down.hide()
        self.up.hide()
        self.start.hide()
