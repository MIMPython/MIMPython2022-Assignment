# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest
# prime factor of the number 600851475143 ?
import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
        return True


def divide_num(num, prime_num):
    while num % prime_num == 0:
        num /= prime_num
    return num


def prime_factor(num):
    num = divide_num(num, 2)
    max_prime = 3
    while num / max_prime >= 1:
        for i in range(max_prime, int(math.sqrt(num)), 2):
            if is_prime(i):
                if num % i == 0:
                    max_prime = i
                    num = divide_num(num, max_prime)
    return max_prime


if __name__ == '__main__':
    number = int(input('Nhập số n: '))
    print(prime_factor(number))
