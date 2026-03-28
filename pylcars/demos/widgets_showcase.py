"""Showcase of all LCARS widgets.

Demonstrates all available widgets with basic usage examples.

Note: For more comprehensive examples, see menu.py which shows
advanced widget composition and interactions.
"""

import sys
from PyQt5 import QtCore, QtWidgets
from pylcars import (
    Lcars,
    Block,
    Bracket,
    Textline,
    Colors,
)


def main() -> None:
    """Display examples of key LCARS widget types."""
    # Create QApplication FIRST, before any widgets
    app = QtWidgets.QApplication(sys.argv)

    # Create the main LCARS window
    window = Lcars()
    window.setWindowTitle("LCARS Widgets Showcase")

    # Title
    title_rect = QtCore.QRect(50, 20, 700, 30)
    title = Textline(window.centralwidget, title_rect, Colors.leuchtblau, 24)
    title.setText("Widget Showcase")

    # Block (solid rectangle)
    block_rect = QtCore.QRect(50, 70, 100, 40)
    block = Block(window.centralwidget, block_rect, Colors.orange)

    # Label for block
    block_label_rect = QtCore.QRect(50, 115, 100, 20)
    block_label = Textline(window.centralwidget, block_label_rect, Colors.beige, 12)
    block_label.setText("Block")

    # Bracket (button)
    button_rect = QtCore.QRect(200, 70, 100, 40)
    button = Bracket(
        window.centralwidget,
        rect=button_rect,
        text="Button",
        color=Colors.rostbraun
    )

    # Another block
    block2_rect = QtCore.QRect(350, 70, 100, 40)
    block2 = Block(window.centralwidget, block2_rect, Colors.apricot)

    # Label for block2
    block2_label_rect = QtCore.QRect(350, 115, 100, 20)
    block2_label = Textline(window.centralwidget, block2_label_rect, Colors.blaugrau, 12)
    block2_label.setText("Decorator")

    # Instructions
    instructions_rect = QtCore.QRect(50, 200, 700, 20)
    instructions = Textline(window.centralwidget, instructions_rect, Colors.rot, 12)
    instructions.setText("For more comprehensive examples, run: python -m pylcars.demos.menu")

    window.show()

    # Run event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
