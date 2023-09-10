#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for victor in matrix:
        for element in victor:
            print("{:d}".format(element), end=" " if element != victor[-1] else "")
        print()
