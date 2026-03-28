"""Test Conditions enumeration."""
from pylcars import Conditions


def test_conditions_exist() -> None:
    """Test that condition constants are defined."""
    assert hasattr(Conditions, "alert")
    assert hasattr(Conditions, "info")
    assert hasattr(Conditions, "use")
    assert hasattr(Conditions, "active")


def test_conditions_are_strings() -> None:
    """Test that all conditions are string values."""
    for condition_name in ["alert", "info", "use", "active"]:
        condition_value = getattr(Conditions, condition_name)
        assert isinstance(condition_value, str)
