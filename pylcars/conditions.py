# -*- coding: utf-8 -*-

from .enumeration import Enumeration
from .colors import Colors


class Conditions(Enumeration):  # type: ignore
    alert: str = Colors.rot
    info: str = Colors.beige
    use: str = Colors.orange
    active: str = Colors.blaugrau
