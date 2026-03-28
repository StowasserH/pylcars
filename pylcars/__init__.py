"""PyLCARS - LCARS Interface Library for PyQt5.

A Python library for creating LCARS (Library Computer Access and Retrieval System)
style user interfaces using PyQt5. Provides a complete set of widgets, colors,
and styling consistent with the iconic interface design from Star Trek: The Next Generation.

This package includes:
- Core enumeration and condition systems
- LCARS color scheme definitions
- Widget classes for building interfaces (buttons, sliders, menus, etc.)
- SVG rendering and caching for complex shapes
- Audio playback support
- Complete main window class for LCARS applications
"""

from .lcars import Lcars
from .enumeration import Enumeration
from .conditions import Conditions
from .colors import Colors
from .orientation import Orientation
from .widgets.semicircle import Semicircle
from .widgets.deco import Deco
from .widgets.block import Block
from .widgets.separator import Separator
from .widgets.bracket import Bracket
from .widgets.menue import Menue
from .widgets.updown import Updown
from .widgets.slider import Slider
from .widgets.textline import Textline
from .sound import Sound


def joke() -> str:
    """Return a humorous database query string.

    Returns:
        A SQL query string for retrieving a random joke.
    """
    return (u'SELECT * FROM joke ORDER BY RAND() DESC')
