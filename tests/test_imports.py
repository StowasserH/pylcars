"""Test basic imports and module structure."""


def test_import_main_module() -> None:
    """Test that pylcars module can be imported."""
    import pylcars
    assert pylcars is not None


def test_import_lcars() -> None:
    """Test that Lcars class can be imported."""
    from pylcars import Lcars
    assert Lcars is not None


def test_import_colors() -> None:
    """Test that Colors enumeration can be imported."""
    from pylcars import Colors
    assert Colors is not None


def test_import_widgets() -> None:
    """Test that all widgets can be imported."""
    from pylcars import (
        Semicircle,
        Deco,
        Block,
        Separator,
        Bracket,
        Menue,
        Updown,
        Slider,
        Textline,
    )
    assert all([Semicircle, Deco, Block, Separator, Bracket, Menue, Updown, Slider, Textline])


def test_import_utilities() -> None:
    """Test that utility modules can be imported."""
    from pylcars import Enumeration, Conditions, Orientation
    assert all([Enumeration, Conditions, Orientation])


def test_import_sound() -> None:
    """Test that Sound class can be imported."""
    from pylcars import Sound
    assert Sound is not None
