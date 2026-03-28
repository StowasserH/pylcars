# -*- coding: utf-8 -*-
from typing import Any, Iterator


class Enumeration(set):
    def __getattr__(self, name: str) -> Any:
        if name in self:
            return name
        raise AttributeError

    def __setattr__(self, name: str, value: Any) -> None:
        raise RuntimeError("Cannot override values")

    def __delattr__(self, name: str) -> None:
        raise RuntimeError("Cannot delete values")

    class __metaclass__(type):
        def __iter__(self) -> Iterator[str]:
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item
