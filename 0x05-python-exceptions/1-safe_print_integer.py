#!/usr/bin/python3
def safe_print_integer(value):
    """Print value if it is integer and dont print if not 

    Args:
        value (int): The number yo be printed

    Return:
        If the value if integer return True or False if not
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

