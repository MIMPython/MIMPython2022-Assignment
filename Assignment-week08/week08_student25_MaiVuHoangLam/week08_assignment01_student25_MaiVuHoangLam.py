import math

def pow(x, y):
    """
    This method is used to calculate exponentiation of a number.


    Arguments:
        x (int): base number
        y (int): exponential number


    Returns:
        result: x to the power of y
    """
    result = math.pow(x, y)
    return result


print(pow(2, 3))  # 8.0
