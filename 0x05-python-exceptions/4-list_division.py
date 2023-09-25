#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Print x elememts of a list.

    Args:
        my_list_1 (list): The list of divident elements.
        my_list_2 (list): The list of divisor elements
        list_length (int): The number of elements of my_list to print.
    Returns:
        New list of results
    """
    nw_lst = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            nw_lst.append(result)
    return nw_lst
