import numpy as np
import sympy as sp
from sympy import *
# # Cách 1
# def fibo(n):
#     if (n < 0):
#         return -1
#     else:
#         if (n == 0 or n == 1):
#             return n
#         else:
#             return fibo(n - 1) + fibo(n - 2)
# n=int(input())
# fibo(n)
# Cách 2
# n=int(input())
# m=int(input())
# khởi tạo ma trận 0
# bạn nhận xét có thể cho mình hỏi là mình dùng np.array thì nó bị lỗi TypeError: 'numpy.int32' object does not support item assignment
# còn nếu dùng np.zeros thì không lỗi. Mình cám ơn
# fibo = np.zeros((n, m), dtype=int) 
# # khởi tạo 2 giá trị ban đầu
# fibo[0 // m  ][0 % m] = 0
# fibo[1 // m  ][1 % m] = 1
# fibo0 = 0
# fibo1 = 1
# # Tạo ma trận số fibo
# for i in range(2, n * m):
#     temp = fibo0 + fibo1
#     fibo[i // m][i % m] = temp
#     fibo0 = fibo1
#     fibo1 = temp
# print(fibo)
# Cách 3
n=int(input())
print(fibonacci(n))
