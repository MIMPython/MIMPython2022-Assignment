# a) Viết một hàm tính ước chung lớn nhất của hai số tự nhiên sử dụng thuật toán Euclid.
from math import comb
from random import randint


def findGCD(a, b):
    if b == 0:
        return a
    return findGCD(b, a % b)

# b) Tính giá trị của P


def probability_of_coprime_integers(n):
    pairs = 10**4
    count = 0
    for i in range(pairs):
        a = randint(1, n)
        b = randint(1, n)
        if findGCD(a, b) == 1:
            count += 1
    return count/pairs


print("Xác suất để hai số bất kì nguyên tố cùng nhau =",
      probability_of_coprime_integers(10**6))  # Xác suất để hai số bất kì nguyên tố cùng nhau = 0.6083
# c) Tìm mối liên hệ giữa giá trị của P và π
# P ~ 6/(pi)**2
