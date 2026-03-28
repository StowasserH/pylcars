# -*- coding: utf-8 -*-
"""Enumeration pattern implementation.

This module provides a flexible enumeration base class that uses a set-based
approach to define enumeration values. It prevents modification of enumeration
values after creation and provides attribute-style access to enumeration members.
"""
from typing import Any, Iterator


class Enumeration(set):
    """A set-based enumeration class that provides attribute access to members.

    This class extends the built-in set to create an enumeration where members
    can be accessed as attributes. The enumeration is immutable - values cannot
    be modified or deleted after creation.

    Example:
        class MyEnum(Enumeration):
            option1: str = "option1"
            option2: str = "option2"

        # Access enum values
        value = MyEnum.option1  # Returns "option1"
    """
    def __getattr__(self, name: str) -> Any:
        """Get enumeration value by attribute name.

        Args:
            name: The name of the enumeration member.

        Returns:
            The enumeration value if the member exists.

        Raises:
            AttributeError: If the member name is not found in the enumeration.
        """
        if name in self:
            return name
        raise AttributeError

    def __setattr__(self, name: str, value: Any) -> None:
        """Prevent modification of enumeration values.

        Args:
            name: The name of the attribute being set.
            value: The value being assigned.

        Raises:
            RuntimeError: Always raised to prevent modification.
        """
        raise RuntimeError("Cannot override values")

    def __delattr__(self, name: str) -> None:
        """Prevent deletion of enumeration values.

        Args:
            name: The name of the attribute being deleted.

        Raises:
            RuntimeError: Always raised to prevent deletion.
        """
        raise RuntimeError("Cannot delete values")

    class __metaclass__(type):
        def __iter__(self) -> Iterator[str]:
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item
