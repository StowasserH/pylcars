"""LCARS color palette showcase.

Displays all available LCARS colors with their names and hex values.
Useful for selecting colors for your LCARS interface.
"""

import sys
from PyQt5 import QtWidgets, QtCore
from pylcars import Lcars, Block, Textline, Colors
from pylcars.config import DEFAULT_WINDOW_HEIGHT, DEFAULT_WINDOW_WIDTH


def main() -> None:
    """Display all LCARS colors with labels and hex values."""
    # Create QApplication FIRST, before any widgets
    app = QtWidgets.QApplication(sys.argv)

    # Create the main LCARS window
    window = Lcars()
    window.setWindowTitle("LCARS Colors")

    # Define all colors with their hex values
    color_list = [
        ("Orange", Colors.orange, "#f90"),
        ("Flieder", Colors.flieder, "#c9c"),
        ("Blaugrau", Colors.blaugrau, "#99c"),
        ("Rostbraun", Colors.rostbraun, "#c66"),
        ("Beige", Colors.beige, "#fc9"),
        ("Leuchtblau", Colors.leuchtblau, "#99f"),
        ("Apricot", Colors.apricot, "#f96"),
        ("Pink", Colors.pink, "#c69"),
        ("Hellorange", Colors.hellorange, "#fc4"),
        ("Rot", Colors.rot, "#c00"),
    ]

    # Create color blocks in a 2x5 grid
    cols = 2
    block_width = (DEFAULT_WINDOW_WIDTH - 60) // cols
    block_height = 40

    for i, (name, color, hex_value) in enumerate(color_list):
        row = i // cols
        col = i % cols

        x = 30 + col * (block_width + 10)
        y = 40 + row * (block_height + 50)

        # Color block (Block: lcars, rect, color, optional style)
        block_rect = QtCore.QRect(x, y, block_width, block_height)
        block = Block(window.centralwidget, block_rect, color)

        # Label with name and hex (Textline: lcars, rect, text_color, text_height)
        label_text = f"{name}: {hex_value}"
        label_rect = QtCore.QRect(x, y + block_height + 5, block_width, 30)
        label = Textline(window.centralwidget, label_rect, Colors.leuchtblau, 14)
        label.setText(label_text)

    window.show()

    # Run event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
