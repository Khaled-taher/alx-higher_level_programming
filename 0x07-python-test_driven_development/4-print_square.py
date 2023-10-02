#!/usr/bin/python3
"""Defining a square printing func."""


def print_square(size):
    """Printing a square with # character.

    Args:
        size (int): The height the square.
    Raises:
        TypeError: When size is not an integer.
        ValueError: When size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
