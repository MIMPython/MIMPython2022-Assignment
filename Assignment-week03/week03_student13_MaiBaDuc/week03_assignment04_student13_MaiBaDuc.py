'''
Bài tập 4. (Fibonacci numbers)
Dãy số Fibonacci {Fn}∞n=0{Fn}n=0∞ được định nghĩa bằng công thức truy hồi:
F0=0,F1=1
Fn+2=Fn+1+Fn ∀n≥0
Viết một chương trình tính số Fibonacci FnFn với một số tự nhiên nn cho trước. 
Hãy giải quyết bài tập này bằng nhiều cách khác nhau, trong đó có cách sử dụng thư viện numpy, sympy.
'''

#Cách 1: dùng vòng lặp
def func_a(x):
    a=0
    b=1
    if(x==0):
        return a
    elif(x==1):
        return b
    else:
        for i in range(2,x+1):
            c = a + b
            a = b
            b = c
        return b

#Cách 2: dùng đệ quy
def func_b(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    else:
        return func_b(x-1) + func_b(x-2)

#Cách 3: dùng ma trận với thư viện numpy
import numpy as np
from numpy import linalg as la
 
def func_c(x):
    arr_1 = np.array([(0,1), (1,1)], dtype=int)
    arr_2 = np.array([0,1], dtype=int)
    arr_3 = (la.matrix_power(arr_1,x))*arr_2
    return(arr_3[0][1])


#Cách 4: dùng đại số với thư viện sympy

from sympy import *

def func_d(x):
    return(fibonacci(x))

x=2
print(func_a(x))
print(func_b(x))
print(func_c(x))
print(func_d(x))