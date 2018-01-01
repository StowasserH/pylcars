import random
from PyQt4 import QtCore, QtGui
import subprocess
from functools import partial

import pylcars
import sys


class LcarsApp(pylcars.Lcars):
    def __init__(self, parent=None):
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
        self.buttons[button_name].tickle(pylcars.Conditions.active)
        self.sound('../Sounds/'+button_name+'.wav')

def main():
    app = QtGui.QApplication(sys.argv)
    form = LcarsApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
