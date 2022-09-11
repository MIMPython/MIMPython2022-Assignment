from math import sqrt
from xmlrpc.client import boolean

def isPrime(num: int) -> boolean:
    """
    This method is used to check if a integer is a prime number.
    
    Arguments:
        num (int): integer to check
        
    Returns:
        result: True if num is prime else False
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print (isPrime(5))