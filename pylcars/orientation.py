# -*- coding: utf-8 -*-
"""Orientation direction constants for LCARS interface elements.

This module defines the cardinal direction constants used to specify the
orientation of UI elements like separators and semicircles in the LCARS interface.
"""

from .enumeration import Enumeration


class Orientation(Enumeration):  # type: ignore
    """Cardinal direction enumeration for widget orientation.

    Defines four cardinal directions used to specify how widgets should be
    oriented or positioned within the interface.

    Attributes:
        left: Left direction (0).
        right: Right direction (1).
        top: Top direction (2).
        bottom: Bottom direction (3).
    """
    left: int = 0
    right: int = 1
    top: int = 2
    bottom: int = 3
