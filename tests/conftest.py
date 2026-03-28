"""Pytest configuration and fixtures for pylcars tests."""
import pytest
from PyQt5 import QtWidgets


@pytest.fixture(scope="session")
def qapp() -> QtWidgets.QApplication:
    """Create a QApplication instance for the test session.

    Returns:
        QtWidgets.QApplication: The Qt application instance.
    """
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication([])
    return app


@pytest.fixture
def main_window(qapp: QtWidgets.QApplication) -> QtWidgets.QMainWindow:
    """Create a main window for testing.

    Args:
        qapp: The Qt application fixture.

    Returns:
        QtWidgets.QMainWindow: A test main window.
    """
    window = QtWidgets.QMainWindow()
    window.resize(800, 480)
    return window
