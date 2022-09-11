import numpy as np

def average(list_):
    """
    This method is used to calculate the average of a list
    
    Library used: numpy
    
    List: 
        list_: a list of integers or floats
    
    Returns:
        result: the result is the average of list_
    
    """
    return np.mean(list_)

print(average([1.2,4,5.1]))