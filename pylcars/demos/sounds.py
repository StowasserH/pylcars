"""Sound playback demonstration for PyLCARS.

A simple demo application showcasing the audio playback capabilities of PyLCARS.
Creates a grid of buttons that play different sound files when clicked.

The demo loads WAV files from a Sounds directory and displays them as
interactive buttons with visual feedback when selected.
"""
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

import pylcars
import sys


class LcarsApp(pylcars.Lcars):
    """Demo application for audio playback with PyLCARS.

    Creates a grid of 60 buttons (10 rows x 6 columns) that correspond to
    sound files. Clicking a button triggers audio playback and provides
    visual feedback through color changes.
    """
    def __init__(self, parent=None):
        """Initialize the sounds demo application.

        Args:
            parent: Parent widget (default: None).
        """
        pylcars.Lcars.__init__(self, parent)
        i = 1
        self.buttons={}
        for row in range(10):
            for col in range(6):
                name = "beep_{num:03d}".format(num=i)
                i = i + 1
                r=QtCore.QRect(10 + 130 * col, 10 + 44 * row, 126, 40)
                button = pylcars.Bracket(self, r, name, pylcars.Conditions.use)
                button.clicked.connect(partial(self.button_callback, button_name=name))
                button.show()
                self.buttons[name]=button
        self.setPlay_sound(True)

    def button_callback(self, button_name):
        """Play a sound file and provide visual feedback.

        Provides visual feedback by tickling the button and plays the
        corresponding sound file from the Sounds directory.

        Args:
            button_name: Name of the button/sound file to play.
        """
        self.buttons[button_name].tickle(pylcars.Conditions.active)
        self.sound('../Sounds/'+button_name+'.wav')

def main():
    """Run the sounds demo application.

    Creates and displays a grid of sound buttons. Each button can be clicked
    to play its corresponding sound file from the Sounds directory.
    """
    app = QtWidgets.QApplication(sys.argv)
    form = LcarsApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
