#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    
    av, div = 0, 0
    for i in my_list:
        av = (i[0] * i[1]) + av
        div = div + i[1]
    return float(av / div)
