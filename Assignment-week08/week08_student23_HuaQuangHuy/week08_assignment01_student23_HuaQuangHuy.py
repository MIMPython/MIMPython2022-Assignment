"""This function is used to find min of pair number x, y

Arguments
    x (int/float): first number
    y (int/float): second number

Returns:
    y if x > y
    x if y >= x
"""


def min(x, y):
    if x > y:
        return y
    else:
        return x
