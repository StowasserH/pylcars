"""Test Orientation enumeration."""
from pylcars import Orientation


def test_orientation_exist() -> None:
    """Test that orientation constants are defined."""
    assert hasattr(Orientation, "left")
    assert hasattr(Orientation, "right")
    assert hasattr(Orientation, "top")
    assert hasattr(Orientation, "bottom")


def test_orientation_are_integers() -> None:
    """Test that all orientations are integer values."""
    for orientation_name in ["left", "right", "top", "bottom"]:
        orientation_value = getattr(Orientation, orientation_name)
        assert isinstance(orientation_value, int)
