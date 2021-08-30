import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Satisfies, Optional
from expyct.base import Instance


@dataclass
class AllOrAny:
    """Mixin for matching a collection object by checking that all or at least
    one of its members are equal to given.

    Like all other `expyct` objects, these can be nested. For example,
    `assert l == exp.AllOrAny(all=exp.Int(min=3))`.

    Attributes:
        all : all members of collection must equal
        any : any member of collection must equal
    """

    all: typing.Optional[typing.Any] = None
    any: typing.Optional[typing.Any] = None

    def __eq__(self, other):
        if self.all is not None:
            if not all(x == self.all for x in other):
                return False
        if self.any is not None:
            if not any(x == self.any for x in other):
                return False
        return True


@dataclass
class Length:
    """Mixin for matching a collection object by its length as the result of len().

    Attributes:
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
    """

    length: typing.Optional[int] = None
    min_length: typing.Optional[int] = None
    max_length: typing.Optional[int] = None
    non_empty: bool = False

    def __eq__(self, other):
        if self.length is not None:
            if not len(other) == self.length:
                return False
        if self.min_length is not None:
            if not len(other) >= self.min_length:
                return False
        if self.max_length is not None:
            if not len(other) <= self.max_length:
                return False
        if self.non_empty:
            if not len(other) > 0:
                return False
        return True


@dataclass
class Contains:
    """Mixin matching a collection object by the containment of specified members.

    Attributes:
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
    """

    superset_of: typing.Optional[typing.Collection] = None
    subset_of: typing.Optional[typing.Collection] = None

    def __eq__(self, other):
        if self.subset_of is not None:
            if isinstance(other, dict) and isinstance(self.subset_of, dict):
                if not all(x in self.subset_of.items() for x in other.items()):
                    return False
            else:
                if not all(x in self.subset_of for x in other):
                    return False

        if self.superset_of is not None:
            if isinstance(other, dict) and isinstance(self.superset_of, dict):
                if not all(x in other.items() for x in self.superset_of.items()):
                    return False
            else:
                if not all(x in other for x in self.superset_of):
                    return False
        return True


@dataclass
class Collection(
    AllOrAny, MapBefore, Optional, Equals[typing.Collection], Instance, Length, Contains, Satisfies
):
    """Match any object that is an instance of `Collection`.

    Attributes:
        all : all members of collection must equal
        any : any member of collection must equal
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        satisfies : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not isinstance(other, typing.Collection):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not AllOrAny.__eq__(self, other):
            return False
        return True


@dataclass
class List(AllOrAny, MapBefore, Optional, Equals[list], Length, Contains, Satisfies):
    """Match any object that is an instance of `list`.

    Attributes:
        all : all members of collection must equal
        any : any member of collection must equal
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        satisfies : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not isinstance(other, list):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not AllOrAny.__eq__(self, other):
            return False
        return True


@dataclass
class Tuple(AllOrAny, MapBefore, Optional, Equals[tuple], Length, Contains, Satisfies):
    """Match any object that is an instance of `tuple`.

    Attributes:
        all : all members of collection must equal
        any : any member of collection must equal
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        satisfies : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not isinstance(other, tuple):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not AllOrAny.__eq__(self, other):
            return False
        return True


@dataclass
class Set(AllOrAny, MapBefore, Optional, Equals[set], Length, Contains, Satisfies):
    """Match any object that is an instance of `set`.

    Attributes:
        all : all members of collection must equal
        any : any member of collection must equal
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        satisfies : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not isinstance(other, set):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not AllOrAny.__eq__(self, other):
            return False
        return True


@dataclass
class Dict(MapBefore, Optional, Equals[dict], Length, Contains, Satisfies):
    """Match any object that is an instance of `dict`.

    Attributes:
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        keys : object keys must equal
        values : object values must equal
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        satisfies : object must satisfy predicate
    """

    keys: typing.Optional[typing.Set] = None
    values: typing.Optional[typing.List] = None
    subset_of: typing.Optional[dict] = None
    superset_of: typing.Optional[dict] = None
    keys_all: typing.Optional[typing.Any] = None
    keys_any: typing.Optional[typing.Any] = None
    values_all: typing.Optional[typing.Any] = None
    values_any: typing.Optional[typing.Any] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not isinstance(other, dict):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if self.keys is not None:
            if not other.keys() == self.keys:
                return False
        if self.values is not None:
            if not other.values() == self.values:
                return False
        if not Contains.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if self.keys_all is not None:
            if not all(x == self.keys_all for x in other.keys()):
                return False
        if self.keys_any is not None:
            if not any(x == self.keys_any for x in other.keys()):
                return False
        if self.values_all is not None:
            if not all(x == self.values_all for x in other.values()):
                return False
        if self.values_any is not None:
            if not any(x == self.values_any for x in other.values()):
                return False
        return True


Dict()

List()
