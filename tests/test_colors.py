"""Test Colors enumeration."""
from pylcars import Colors


def test_colors_exist() -> None:
    """Test that color constants are defined."""
    assert hasattr(Colors, "orange")
    assert hasattr(Colors, "flieder")
    assert hasattr(Colors, "blaugrau")
    assert hasattr(Colors, "rostbraun")
    assert hasattr(Colors, "beige")
    assert hasattr(Colors, "leuchtblau")
    assert hasattr(Colors, "apricot")
    assert hasattr(Colors, "pink")
    assert hasattr(Colors, "hellorange")
    assert hasattr(Colors, "rot")


def test_colors_are_valid_hex() -> None:
    """Test that all colors are valid hex color values."""
    for color_name in [
        "orange",
        "flieder",
        "blaugrau",
        "rostbraun",
        "beige",
        "leuchtblau",
        "apricot",
        "pink",
        "hellorange",
        "rot",
    ]:
        color_value = getattr(Colors, color_name)
        assert isinstance(color_value, str)
        assert color_value.startswith("#")
        assert len(color_value) == 4  # 3-digit hex like #f90
