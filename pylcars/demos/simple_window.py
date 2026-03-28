"""Minimal LCARS window example.

This is the simplest possible example of creating a LCARS interface.
It demonstrates basic window setup and adding a simple button widget.
"""

from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket, Colors


def main() -> None:
    """Create and display a minimal LCARS window with a single button."""
    app = QtWidgets.QApplication([])

    # Create the main LCARS window
    window = Lcars()
    window.setWindowTitle("Simple LCARS Window")

    # Add a button to the central widget
    button = Bracket(window.centralwidget)
    button.setText("HELLO LCARS")
    button.set_color(Colors.orange)
    button.setGeometry(300, 200, 200, 80)

    # Show and run
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
