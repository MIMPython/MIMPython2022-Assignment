#Bài 4
#Sử dụng numpy
"""
fn = [(((1+sqrt(5))/2)**n - (((1-sqrt(5))/2)**n]*(1/sqrt(5))]
alpha = (1+sqrt(5))/2
beta = (1-sqrt(5))/2
"""
import numpy as np

n = int(input("n="))
a = np.arange(1,n+1) 

sqrt5 = np.sqrt(5)
b = (1+ sqrt5)/2
c = (1- sqrt5)/2
fn = (b**a - c**a)/sqrt5
Fn = np.rint(fn) #Làm tròn thành số nguyên
print(Fn)

#Sử dụng sympy
from sympy import * 
n = int(input("n="))
A = []
for i in range(1,n+1):
    d = fibonacci(i)
    A.append(d)
print(A)
