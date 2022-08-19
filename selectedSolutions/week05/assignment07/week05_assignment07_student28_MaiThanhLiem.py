import itertools
from math import sqrt


def isPalindromeNumber(number: int):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def isSquareNumber(number: int):
    if sqrt(number) - int(sqrt(number)) == 0:
        return True
    else:
        return False


for number in itertools.count(0):
    if isPalindromeNumber(number) and isSquareNumber(number):
        print(number)

"""
The number of Palindrome square number is indeed infinite.
Notice that numbers express as (10^n + 1)^2, for all integer n, is  is always Palindrome:
(10^n + 1)^2 = 10^2n + 2*10^n + 1 = 1000...02000...01 (n-1 zeros each side).
"""
