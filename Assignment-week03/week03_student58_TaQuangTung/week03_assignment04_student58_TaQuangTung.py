print("Bài 4: Fibonacci numbers")
print()


#Dùng numpy tính dãy Fibonacci
print("Cách 1: Sử dụng numpy")
"""
fn = [((1+sqrt(5))/2)^n - ((1-sqrt(5))/2)^n]*(1/sqrt(5))
a = (1+sqrt(5))/2, b = (1-sqrt(5))/2
"""
import numpy as np
from sympy import fibonacci

n = int(input("Nhập n = "))
a = np.arange(1, n+1)     #mảng từ 1 --> n-1
lengtha = len(a)        #độ dài mảng a

#Áp dụng công thức
cannam = np.sqrt(5)
alpha = (1 + cannam)/2
beta = (1 -cannam)/2

kq = ((alpha**a) - (beta**a))/cannam
#Hàm np.rint() để làm tròn thành số nguyên
Fn = np.rint(kq)
print(Fn)
print()


#Dùng simpy tính dãy Fibonacci
print("Cách 2: Sử dụng simpy")
N = int(input("Nhập n = "))
lst = []
for i in range(1, N+1):
    fib = fibonacci(i)
    lst.append(fib)
print(lst)
print()


#Sử dụng vòng lặp cơ bản
print("Cách 3: Sử dụng vòng lặp mảng")

def fibonacilist(n):
    lt = []
    if n == 1:
        lt.append(1)
    if n > 1:
        f0 = 0
        f1 = 1
        lt.append(1)
        for i in range(2,n+1):
            f = f0 + f1
            lt.append(f)
            f0 = f1
            f1 = f
    return lt
n = int(input("Nhập n = "))
print("Theo mảng list =",fibonacilist(n))
print()


#Sử dụng đệ quy
print("Cách 4: Sử dụng đệ quy")
def dequyfib(n):
    f0 = 0
    f1 = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return dequyfib(n-2) + dequyfib(n-1)
n = int(input("Nhập số n = "))
for i in range(n+1):
    print(dequyfib(i),end = " ")