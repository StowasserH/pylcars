# -*- coding: utf-8 -*-

from .enumeration import Enumeration


class Orientation(Enumeration):  # type: ignore
    left: int = 0
    right: int = 1
    top: int = 2
    bottom: int = 3
