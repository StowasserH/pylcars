"""Custom theme example for LCARS interface.

Demonstrates how to customize fonts, colors, and other styling
to create a unique LCARS interface variant.
"""

from PyQt5 import QtWidgets, QtGui
from pylcars import Lcars, Bracket, Block, Slider, Colors


def main() -> None:
    """Create a LCARS window with custom styling."""
    app = QtWidgets.QApplication([])

    window = Lcars()
    window.setWindowTitle("Custom Theme Example")

    # Customize widget font size
    custom_font = QtGui.QFont()
    custom_font.setFamily("LCARS")
    custom_font.setPointSize(32)

    # Button with custom styling
    button1 = Bracket(window.centralwidget)
    button1.set_color("#99f")  # Bright blue instead of standard colors
    button1.setText("CUSTOM")
    button1.setFont(custom_font)
    button1.setGeometry(100, 100, 150, 60)

    # Alternative color scheme button
    button2 = Bracket(window.centralwidget)
    button2.set_color("#f0f")  # Magenta (not standard LCARS)
    button2.setText("THEME")
    button2.setGeometry(300, 100, 150, 60)

    # Custom styled block with gradient-like effect
    block1 = Block(window.centralwidget)
    block1.set_color("#0f0")  # Lime green
    block1.setGeometry(100, 200, 100, 50)

    block2 = Block(window.centralwidget)
    block2.set_color("#00f")  # Pure blue
    block2.setGeometry(250, 200, 100, 50)

    # Slider with custom color
    slider = Slider(window.centralwidget)
    slider.set_color("#ff0")  # Yellow
    slider.setGeometry(100, 300, 350, 40)

    # Information text
    info = Bracket(window.centralwidget)
    info.set_color(Colors.leuchtblau)
    info.setText("Custom colors")
    info.setGeometry(100, 380, 350, 50)

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
