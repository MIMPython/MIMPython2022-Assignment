import numpy as np
import random
from time import perf_counter


# 1a)
def foo(row, column):
    a = []
    for i in range(0, row):
        b = []
        for j in range(0, column):
            b += [random.randint(0, 10)]
        a += [b]
    return a


m = int(input())
n = int(input())
array = foo(m, n)


# 1b)
def bar(array):
    result = []
    sum = 0
    for i in range(0, len(array[0])):
        for j in range(0, len(array)):
            sum += array[j][i]
        result.append(sum)
        sum = 0
    return result


# # 1c)
# def foo(row, column):
#     a = np.random.randint(0, 10, (row, column))
#     return a
#
#
# def bar_column(array):
#     return np.sum(array, 0)


# 1d)


# 1e)
def bar_row(array):
    return np.sum(array, 1)




