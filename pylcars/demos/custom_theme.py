"""Custom theme example for LCARS interface.

Demonstrates how to use custom colors and styling to create
a unique LCARS interface variant.
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from pylcars import Lcars, Bracket, Block, Textline, Colors


def main() -> None:
    """Create a LCARS window with custom styling."""
    # Create the main LCARS window
    window = Lcars()
    window.setWindowTitle("Custom Theme Example")

    # Define custom colors (non-standard LCARS colors)
    class CustomColors:
        bright_blue = "#00ffff"    # Cyan
        bright_green = "#00ff00"   # Lime
        magenta = "#ff00ff"        # Magenta
        yellow = "#ffff00"         # Yellow

    # Custom styled button
    button1_rect = QtCore.QRect(100, 100, 150, 60)
    button1 = Bracket(
        window.centralwidget,
        rect=button1_rect,
        text="CUSTOM",
        color=CustomColors.bright_blue
    )

    # Alternative color scheme button
    button2_rect = QtCore.QRect(300, 100, 150, 60)
    button2 = Bracket(
        window.centralwidget,
        rect=button2_rect,
        text="THEME",
        color=CustomColors.magenta
    )

    # Custom styled blocks
    block1_rect = QtCore.QRect(100, 200, 100, 50)
    block1 = Block(window.centralwidget, block1_rect, CustomColors.bright_green)

    block2_rect = QtCore.QRect(250, 200, 100, 50)
    block2 = Block(window.centralwidget, block2_rect, CustomColors.yellow)

    # Information text
    info_rect = QtCore.QRect(100, 300, 350, 50)
    info = Textline(window.centralwidget, info_rect, Colors.leuchtblau, 16)
    info.setText("Custom colors")

    window.show()

    # Get or create QApplication
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
