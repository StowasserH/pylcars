"""Showcase of all LCARS widgets.

Demonstrates all available widgets with basic usage examples.
"""

from PyQt5 import QtWidgets
from pylcars import (
    Lcars,
    Block,
    Bracket,
    Deco,
    Separator,
    Slider,
    Textline,
    Updown,
    Colors,
)


def main() -> None:
    """Display examples of all LCARS widget types."""
    app = QtWidgets.QApplication([])

    window = Lcars()
    window.setWindowTitle("LCARS Widgets Showcase")

    # Title
    title = Textline(window.centralwidget)
    title.setText("Widget Showcase")
    title.set_color(Colors.leuchtblau)
    title.setGeometry(50, 20, 700, 30)

    # Block (solid rectangle)
    block = Block(window.centralwidget)
    block.set_color(Colors.orange)
    block.setGeometry(50, 70, 100, 40)

    block_label = Textline(window.centralwidget)
    block_label.setText("Block")
    block_label.set_color(Colors.beige)
    block_label.setGeometry(50, 115, 100, 20)

    # Bracket (button)
    bracket = Bracket(window.centralwidget)
    bracket.setText("Button")
    bracket.set_color(Colors.rostbraun)
    bracket.setGeometry(200, 70, 100, 40)

    # Deco (decorative label)
    deco = Deco(window.centralwidget)
    deco.setText("Deco")
    deco.set_color(Colors.apricot)
    deco.setGeometry(350, 70, 100, 40)

    # Separator
    separator = Separator(window.centralwidget)
    separator.set_color(Colors.flieder)
    separator.setGeometry(500, 70, 5, 120)

    # Slider (horizontal)
    slider = Slider(window.centralwidget)
    slider.set_color(Colors.leuchtblau)
    slider.setGeometry(50, 180, 300, 40)

    slider_label = Textline(window.centralwidget)
    slider_label.setText("Slider")
    slider_label.set_color(Colors.blaugrau)
    slider_label.setGeometry(50, 225, 100, 20)

    # Updown (navigation control)
    updown = Updown(window.centralwidget)
    updown.set_color(Colors.hellorange)
    updown.setGeometry(400, 180, 100, 80)

    updown_label = Textline(window.centralwidget)
    updown_label.setText("UpDown")
    updown_label.set_color(Colors.pink)
    updown_label.setGeometry(400, 265, 100, 20)

    # Instructions
    instructions = Textline(window.centralwidget)
    instructions.setText("Interact with widgets to see effects")
    instructions.set_color(Colors.rot)
    instructions.setGeometry(50, 320, 700, 20)

    instructions2 = Textline(window.centralwidget)
    instructions2.setText("Close window to exit")
    instructions2.set_color(Colors.rot)
    instructions2.setGeometry(50, 345, 700, 20)

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
