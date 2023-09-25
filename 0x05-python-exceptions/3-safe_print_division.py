#!/usr/bin/python3
def safe_print_division(a, b):
    """Print the result of division of two integer using {}.format

    Args:
        a: the dividant of the equation
        b: the divisor of the equation

    Return:
        If the result if availiable return it
        Otherwise return None
    """
    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
