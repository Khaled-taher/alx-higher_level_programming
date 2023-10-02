#!/usr/bin/python3
"""Defining a name printing func."""


def say_my_name(first_name, last_name=""):
    """Print name.

    Args:
        first_name (str): first printed name.
        last_name (str): last printed name.
    Raises:
        TypeError: When first_name-last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
