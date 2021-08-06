import typing
from dataclasses import dataclass

from expyct.base import MapBefore, Predicate, Instance, Class, Equals


@dataclass
class Any(MapBefore, Equals[typing.Any], Predicate):
    """Match any object.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        pred : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class AnyValue(Any, Instance):
    def __eq__(self, other):
        if not Any.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
        return True


@dataclass
class AnyClass(Any, Class):
    def __eq__(self, other):
        if not Any.__eq__(self, other):
            return False
        if not Class.__eq__(self, other):
            return False
        return True


ANY = Any()
ANYVALUE = AnyValue()
ANYCLASS = AnyClass()
