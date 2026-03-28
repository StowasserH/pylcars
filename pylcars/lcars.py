"""Main LCARS window class for PyQt5 applications.

This module provides the primary window class for creating LCARS-themed
interfaces. It combines PyQt5's main window functionality with audio playback
capabilities through the Sound class.
"""
from typing import Optional
from PyQt5 import QtCore, QtWidgets
from .sound import Sound
from .config import DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT


class Lcars(Sound, QtWidgets.QMainWindow):
    """Main window class for LCARS-themed PyQt5 applications.

    Combines PyQt5's QMainWindow with audio playback functionality to create
    a complete LCARS interface base. Handles window setup, styling, and provides
    a central widget for placing UI elements.

    Attributes:
        default_style: Default stylesheet for the main window (transparent with black background).
        mainWindowSize: Size of the main window (default: 800x480).
        centralwidget: The central widget of the main window.
    """
    default_style: str = "border: none;\nbackground: #000;\n"
    mainWindowSize: QtCore.QSize
    centralwidget: QtWidgets.QWidget

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Set up the main window UI.

        Configures the window properties, applies default styling, creates the
        central widget, and initializes signal-slot connections.

        Args:
            MainWindow: The main window to configure.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.mainWindowSize)
        MainWindow.setStyleSheet(self.default_style)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Set window title and other translatable strings.

        Args:
            MainWindow: The main window to configure.
        """
        MainWindow.setWindowTitle("MainWindow")

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None) -> None:
        """Initialize the LCARS main window.

        Creates a new LCARS main window with the specified parent. Initializes
        both QMainWindow and Sound functionality, sets up the default window size
        (800x480), and performs initial UI setup.

        Args:
            parent: Parent widget (default: None for top-level window).
        """
        QtWidgets.QMainWindow.__init__(self, parent)
        Sound.__init__(self)
        self.mainWindowSize = QtCore.QSize(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
        self.setupUi(self)
