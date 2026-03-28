"""LCARS color palette showcase.

Displays all available LCARS colors with their names and hex values.
Useful for selecting colors for your LCARS interface.
"""

from PyQt5 import QtWidgets, QtCore
from pylcars import Lcars, Block, Textline, Colors
from pylcars.config import DEFAULT_WINDOW_HEIGHT, DEFAULT_WINDOW_WIDTH


def main() -> None:
    """Display all LCARS colors with labels and hex values."""
    app = QtWidgets.QApplication([])

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

        # Color block
        block = Block(window.centralwidget)
        block.set_color(color)
        block.setGeometry(x, y, block_width, block_height)

        # Label with name and hex
        label = Textline(window.centralwidget)
        label.setText(f"{name}: {hex_value}")
        label.set_color(Colors.leuchtblau)
        label.setGeometry(x, y + block_height + 5, block_width, 30)

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
