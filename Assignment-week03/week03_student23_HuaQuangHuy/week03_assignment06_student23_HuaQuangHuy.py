# Bài tập 6
# N = 10^3
# a, viết hàm thực hiện ước chung lớn nhất bằng thuật toán Euclid:
import more_itertools as itertools


def getGCD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a


if __name__ == '__main__':
    print(getGCD(15, 12))
    list = range(0, 10**3)
    copu = itertools.distinct_combinations(list, 2) # get combinations from 10^3 element
    sum = 0
    sumSatisfy = 0
    for e in copu:
        a = e[0]
        b = e[1]
        gcd = getGCD(a, b)
        if gcd == 1:
            sumSatisfy += 1
        sum += 1

    print(f"Probability: {sumSatisfy / sum}") # 0.6081921921921922
