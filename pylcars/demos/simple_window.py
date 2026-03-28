"""Minimal LCARS window example.

This is the simplest possible example of creating a LCARS interface.
It demonstrates basic window setup and adding a simple button widget.
"""

import sys
from PyQt5 import QtCore, QtWidgets
from pylcars import Lcars, Bracket, Colors


def main() -> None:
    """Create and display a minimal LCARS window with a single button."""
    # Create QApplication FIRST, before any widgets
    app = QtWidgets.QApplication(sys.argv)

    # Create the main LCARS window
    window = Lcars()
    window.setWindowTitle("Simple LCARS Window")

    # Create a button with required parameters: parent, rect, text, color
    button_rect = QtCore.QRect(300, 200, 200, 80)
    button = Bracket(
        window.centralwidget,
        rect=button_rect,
        text="HELLO LCARS",
        color=Colors.orange
    )

    # Show the window
    window.show()

    # Run event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
