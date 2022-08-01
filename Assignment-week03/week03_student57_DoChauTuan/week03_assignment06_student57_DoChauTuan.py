# Bài tập 6. (probability of coprime integers)
import numpy as np


def prob_coprime(n):
    prob = 0
    for i in range(1, n + 1):
        prob = prob + (1 / i ** 2)
    return 1 / prob


def find_argument(prob, epsilon):
    b = 0
    while prob - int(prob) > epsilon:
        prob = prob * np.pi
        b += 1
    return (int(prob), b)


def gcd(a, b):
    while b:
        tmp = a % b
        a = b
        b = tmp
    return a


def counted_coprime(n):
    coprime = 0
    for i in range(1, n):
        for j in range(i, n + 1):
            if gcd(i, j) == 1:
                coprime += 1
    return coprime / n ** 2


if __name__ == "__main__":
    print(f"Solution 1 : {prob_coprime(1000000)}")  # Solution 1: 0.6079274714294116
    print(f"Solution 2 : {counted_coprime(1000000)}")  # Solution 2: 0.6079274714294116
    print(find_argument(prob_coprime(1000000), 1e-2))  # (6, 2)

# Reference : https://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml



