# -*- coding: utf-8 -*-
"""Menu widget for page navigation and content switching.

This module implements the Menue widget, a comprehensive menu system with
multiple pages, navigation buttons, and visual separators for managing
interface content display.
"""
from typing import Any, Callable, Dict, List, Optional

from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from .separator import Separator
from ..conditions import Conditions
from ..orientation import Orientation
from .bracket import Bracket
from .block import Block
from functools import partial


class Menue:
    """A multi-page menu system with buttons and content pages.

    Manages a menu with multiple button tabs and associated content pages.
    Each button can be selected to display its associated page content.
    Supports visual feedback, dynamic color changes, and custom callbacks.

    Attributes:
        lcars: Reference to parent LCARS window.
        color: Primary menu color.
        color_active: Color when menu item is active.
        enabled: Whether the menu is currently enabled.
        buttons: Dictionary mapping button names to Bracket button widgets.
        pages: Dictionary mapping page names to content widget dictionaries.
        fields: List of button/page names in order.
        top: Top separator decoration.
        bot: Bottom separator decoration.
        linetop: Top line decoration.
        linebot: Bottom line decoration.
        fill: Fill decoration.
        active_page: Name of the currently displayed page.
        button_callback: Function called when a button is clicked.
    """
    lcars: QtWidgets.QWidget
    color: str
    color_active: str
    enabled: bool
    buttons: Dict[str, Bracket]
    pages: Dict[str, Dict[str, Any]]
    fields: List[str]
    top: Separator
    bot: Separator
    linetop: Block
    linebot: Block
    fill: Block
    active_page: str
    button_callback: Callable[[str], None]

    def menu_click(self, button_name: str = "\n") -> None:
        """Handle menu button click and page switching.

        Switches to the selected page if the menu is enabled and the page
        is different from the current one. Provides visual feedback through
        color toggling and plays a sound effect.

        Args:
            button_name: Name of the button/page to switch to.
        """
        if not self.enabled:
            return
        if self.active_page != button_name:
            self.lcars.play_sound()
            self.blend_out(self.active_page)
            self.buttons[self.active_page].tockle()
            self.active_page = button_name
            self.buttons[self.active_page].tockle(self.color_active)
            self.blend_in(self.active_page)

    def blend_out(self, page: str) -> None:
        """Hide all widgets on a page.

        Args:
            page: Name of the page whose widgets should be hidden.
        """
        widgets = self.pages[page]
        for widget in widgets:
            widgets[widget].hide()

    def blend_in(self, page: str) -> None:
        """Show all widgets on a page.

        Args:
            page: Name of the page whose widgets should be shown.
        """
        widgets = self.pages[page]
        for widget in widgets:
            widgets[widget].show()

    def paint_back(self, color: str) -> None:
        """Change menu color for all decorative elements.

        Updates the color of all menu buttons and decorative elements
        (separators and lines).

        Args:
            color: New color for the menu elements.
        """
        for button in self.fields:
            self.buttons[button].paint_back(color)
        self.top.paint_back(color)
        self.bot.paint_back(color)
        self.linetop.paint_back(color)
        self.linebot.paint_back(color)
        self.fill.paint_back(color)

    def setEnabled(self, enabled: bool) -> None:
        """Enable or disable menu interaction.

        Args:
            enabled: True to enable menu interaction, False to disable.
        """
        self.enabled = enabled

    def __init__(self, lcars: QtWidgets.QWidget, fields: List[str], rect: QtCore.QRect, button_size: QtCore.QSize, color_use: str = Conditions.use,
                 color_active: str = Conditions.active, button_space: int = 4, button_callback: Optional[Callable[[str], None]] = None) -> None:
        """Initialize a Menu widget.

        Creates a menu with buttons for each field and associated pages.
        Includes decorative separators and lines. The first field is
        displayed as the active page by default.

        Args:
            lcars: Parent LCARS window.
            fields: List of button/page names to create.
            rect: Geometry rectangle for the entire menu.
            button_size: Size of each button widget.
            color_use: Color for normal button state (default: Conditions.use).
            color_active: Color for active button state (default: Conditions.active).
            button_space: Spacing between buttons in pixels (default: 4).
            button_callback: Optional custom callback function for button clicks.
                If not provided, uses the default menu_click method.
        """
        self.lcars: QtWidgets.QWidget = lcars
        self.color = color_use
        self.color_active = color_active
        self.enabled = True
        rx: int = rect.x()
        ry: int = rect.y()
        rh: int = rect.height()
        rw: int = rect.width()
        bw: int = button_size.width()
        bh: int = button_size.height()
        seperator_width: int = int(bw + bw / 2)
        self.top = Separator(lcars, QtCore.QRect(rx, ry, seperator_width, bh), color_use, bw,
                             orientation=Orientation.top)
        self.buttons = {}
        self.pages = {}
        self.fields = fields
        pos = bh + button_space
        self.button_callback = button_callback if button_callback else self.menu_click
        for button in self.fields:
            self.buttons[button] = Bracket(lcars, QtCore.QRect(rx, pos, bw, bh), button + " ", color_use)
            self.buttons[button].clicked.connect(partial(self.button_callback, button_name=button))
            pos += bh + button_space
            self.pages[button] = {}
        self.active_page = fields[0]
        self.buttons[self.active_page].tockle(Conditions.active)
        self.bot = Separator(lcars, QtCore.QRect(rx, rh - bh, seperator_width, bh), color_use, bw,
                             orientation=Orientation.bottom)
        lx: int = rx + seperator_width + button_space
        lw: int = rw - lx

        self.linetop = Block(lcars, QtCore.QRect(lx, ry, lw, int(bh / 2)), Conditions.use)
        bs: int = int(rh - bh / 2)
        self.linebot = Block(lcars, QtCore.QRect(lx, bs, lw, int(bh / 2)), Conditions.use)
        # pos += bh + button_space
        self.fill = Block(lcars, QtCore.QRect(rx, pos, bw, int(rh - bh - pos - button_space)), Conditions.use)
