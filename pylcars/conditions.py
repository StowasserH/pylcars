# -*- coding: utf-8 -*-
"""Status condition color mapping for LCARS interface elements.

This module defines the semantic status conditions used in LCARS interface
elements and maps them to appropriate colors from the LCARS color palette.
These conditions represent different states that interface widgets can have.
"""

from .enumeration import Enumeration
from .colors import Colors


class Conditions(Enumeration):  # type: ignore
    """Enumeration of interface element status conditions.

    Maps semantic status conditions to LCARS colors for consistent visual
    representation across the interface. Each condition conveys a specific
    state or purpose for interface elements.

    Attributes:
        alert: Alert/critical state mapped to red color.
        info: Informational state mapped to beige color.
        use: Usable/available state mapped to orange color.
        active: Active/selected state mapped to blue-gray color.
    """
    alert: str = Colors.rot
    info: str = Colors.beige
    use: str = Colors.orange
    active: str = Colors.blaugrau
