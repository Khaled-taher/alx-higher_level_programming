#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as me:
        print("Exception: {}".format(me), file=sys.stderr)
        return (False)
