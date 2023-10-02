#!/usr/bin/python3
"""Defining an integer adding func."""


def add_integer(a, b=98):
    """Return an integer add of a and b.

    Float arguments are casted to inegers before addition.

    Raises:
        TypeError: If a or b is a not integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
