"""Menu and widget demonstration for PyLCARS.

A comprehensive demo application showcasing the various widgets and features
of the PyLCARS library, including menus, buttons, sliders, decorative elements,
and interactive controls with visual feedback.

Run this demo to see a fully functional LCARS interface with multiple pages
and interactive elements.
"""
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
from functools import partial

import pylcars
import sys


class LcarsApp(pylcars.Lcars):
    """Demo application showcasing PyLCARS widgets and features.

    A full-featured demo that displays multiple pages of LCARS widgets including
    buttons, sliders, decorative elements, and controls. Features include:
    - Multi-page menu system
    - Interactive button controls
    - Horizontal and vertical sliders
    - Custom SVG rendering examples
    - Exit/shutdown sequence demo
    """
    def exit_to_desk(self):
        """Exit the application to desktop.

        Terminates the application cleanly.
        """
        exit(0)

    def exit_to_shutdown(self):
        """Engage self-destruct sequence and exit after delay.

        Displays a self-destruct message, disables the menu, and schedules
        application exit after a 3-second countdown.
        """
        self.exit_desk.hide()
        self.exit_down.hide()
        self.shutdown.show()
        self.menue.setEnabled(False)
        subprocess.Popen('echo "enter your shutdown script"', shell=True)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.exit_to_desk)
        timer.setSingleShot(True)
        timer.start(3000)

    def __init__(self, parent=None):
        """Initialize the demo application with all pages and widgets.

        Args:
            parent: Parent widget (default: None).
        """
        pylcars.Lcars.__init__(self, parent)
        self.qurrent_title_timer = QtCore.QTimer(self)
        fields = ('BUTTONS', 'DECO', 'SLIDER', 'EXIT')
        self.menue = pylcars.Menue(self, fields, QtCore.QRect(0, 0, 800, 480), QtCore.QSize(130, 40),
                                   button_callback=self.menu_click)
        # _________________________________________________________________
        #
        #   The Slider -Page
        # _________________________________________________________________
        self.vslider = pylcars.Slider(self, QtCore.QRect(140, 44, 180, 40), QtCore.Qt.Horizontal)
        self.vslider.setInvertedAppearance(True)
        self.vslider.setInvertedControls(True)
        self.vslider.hide()
        self.menue.pages['SLIDER']['slider'] = self.vslider

        self.hslider = pylcars.Slider(self, QtCore.QRect(140, 84, 40, 180), QtCore.Qt.Vertical)
        self.hslider.setInvertedAppearance(True)
        self.hslider.setInvertedControls(True)
        self.hslider.hide()
        self.menue.pages['SLIDER']['hslider'] = self.hslider

        # _________________________________________________________________
        #
        #   The Buttons -Page
        # _________________________________________________________________

        self.updown = pylcars.Updown(self, QtCore.QRect(140, 44, 180, 40), "0 ")
        self.updown.hide()
        self.menue.pages['BUTTONS']['updown'] = self.updown
        self.updown.down.clicked.connect(self.updown_down)
        self.updown.up.clicked.connect(self.updown_up)
        self.updown.start.clicked.connect(self.updown_click)

        self.updown2 = pylcars.Updown(self, QtCore.QRect(340, 44, 180, 40), text="0 ")
        self.updown2.hide()
        self.menue.pages['BUTTONS']['updown2'] = self.updown2
        self.updown2.down.clicked.connect(self.updown2_down)
        self.updown2.up.clicked.connect(self.updown2_up)
        self.updown2.start.clicked.connect(self.updown2_click)

        self.buttons = {}

        self.colors = {}
        for color in pylcars.Colors.__dict__.items():
            if not color[0].startswith('_'):
                self.colors[color[0]] = color[1]
        for row in range(8):
            self.buttons[row] = {}
            for col in range(4):
                name, color = random.choice(list(self.colors.items()))
                buttonname = "{r}_{c}".format(r=row, c=col)
                self.buttons[row][col] = pylcars.Bracket(self, QtCore.QRect(140 + 160 * col, 88 + 44 * row, 156, 40)
                                                         , "{c} {n}".format(c=name, n=buttonname), color)
                self.buttons[row][col].hide()
                self.menue.pages['BUTTONS'][buttonname] = self.buttons[row][col]
                self.buttons[row][col].clicked.connect(partial(self.button_callback, button_name=buttonname))

        # _________________________________________________________________
        #
        #   The Deco -Page
        # _________________________________________________________________

        svg = '<svg height="200" width="200">' \
              '<circle cx="100" cy="100" r="100" fill="{c1}" />' \
              '<rect height="200" width="10" x="95" y="0" fill="#000" />' \
              '<rect height="10" width="200" x="0" y="95" fill="#000" />' \
              '<circle cx="100" cy="100" r="50" fill="#000" />' \
              '<circle cx="100" cy="100" r="25" fill="{c2}" />' \
              '</svg>'.format(c1=pylcars.Conditions.alert, c2=pylcars.Conditions.use)

        self.deco = pylcars.Deco(self, QtCore.QRect(300, 100, 200, 200), pylcars.Conditions.alert, svg=svg)
        self.deco.hide()
        self.menue.pages['DECO']['deco'] = self.deco

        # _________________________________________________________________
        #
        #   The Exit -Page
        # _________________________________________________________________

        self.alert = False
        style = "border: none;\nbackground: {bg};\ncolor: " + pylcars.Conditions.alert + ";\nqproperty-alignment: AlignCenter;"
        self.shutdown = pylcars.Deco(self, QtCore.QRect(140, 100, 640, 300), pylcars.Conditions.alert, style=style)
        destruct_font = QtGui.QFont()
        self.default_font_name = "LCARS"
        destruct_font.setFamily(self.shutdown.default_font_name)
        destruct_font.setPointSize(80)
        destruct_font.setBold(True)
        destruct_font.setStrikeOut(False)
        # self.shutdown.setStyleSheet(self.shutdown.style)
        self.shutdown.setFont(destruct_font)
        self.shutdown.setText("SELF DESTRUCT\nSEQUENCE ENGAGED")
        self.shutdown.hide()
        self.exit_desk = pylcars.Bracket(self, QtCore.QRect(200, 120, 400, 100), "Exit to Desktop ",
                                         pylcars.Conditions.use)
        self.exit_desk.clicked.connect(self.exit_to_desk)
        self.exit_down = pylcars.Bracket(self, QtCore.QRect(200, 260, 400, 100), "ENGAGE SELF DESTRUCT SEQUENCE ",
                                         pylcars.Conditions.alert)
        self.exit_down.clicked.connect(self.exit_to_shutdown)
        self.menue.pages['EXIT']['exit_desk'] = self.exit_desk
        self.menue.pages['EXIT']['exit_down'] = self.exit_down
        self.exit_desk.hide()
        self.exit_down.hide()
        # _________________________________________________________________
        #
        #   End of the initialisation
        # _________________________________________________________________

    def menu_click(self, button_name):
        """Handle menu page navigation with color feedback.

        Changes menu color to alert when navigating to EXIT page,
        and back to normal for other pages.

        Args:
            button_name: Name of the page to navigate to.
        """
        if not self.menue.enabled:
            return
        if button_name == 'EXIT':
            self.menue.menu_click(button_name)
            if not self.alert:
                self.alert = True
                self.menue.paint_back(pylcars.Conditions.alert)
        else:
            if self.alert:
                self.alert = False
                self.menue.paint_back(pylcars.Conditions.use)
            self.menue.menu_click(button_name)

    def button_callback(self, button_name):
        """Provide visual feedback when buttons are clicked.

        Randomly toggles or tickles a button with a random color.

        Args:
            button_name: Name of the button that was clicked.
        """
        name, color = random.choice(list(self.colors.items()))
        if random.choice((1, 2)) == 1:
            self.menue.pages['BUTTONS'][button_name].tockle(color)
        else:
            self.menue.pages['BUTTONS'][button_name].tickle(color)

    def updown_down(self):
        """Decrement the first updown counter."""
        self.updown.start.setText(str(int(self.updown.start.text()) - 1) + " ")

    def updown_up(self):
        """Increment the first updown counter."""
        self.updown.start.setText(str(int(self.updown.start.text()) + 1) + " ")

    def updown_click(self):
        """Reset the first updown counter to zero."""
        self.updown.start.setText("0 ")

    def updown2_down(self):
        """Decrement the second updown counter with visual feedback."""
        self.updown2.down.tickle(pylcars.Conditions.active)
        self.updown2.start.setText(str(int(self.updown2.start.text()) - 1) + " ")

    def updown2_up(self):
        """Increment the second updown counter with visual feedback."""
        self.updown2.up.tickle(pylcars.Conditions.active)
        self.updown2.start.setText(str(int(self.updown2.start.text()) + 1) + " ")

    def updown2_click(self):
        """Reset the second updown counter to zero with color toggle."""
        self.updown2.start.tockle(pylcars.Conditions.active)
        self.updown2.start.setText("0 ")


def main():
    """Run the menu demo application.

    Creates and displays the demo LCARS interface with all widgets and pages.
    """
    app = QtWidgets.QApplication(sys.argv)
    form = LcarsApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
