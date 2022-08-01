
# Quy ước: trả về -1 nghĩa là số không tồn tại

#Cách 1:
def fibonacci_1(n):
    f0 = 0
    f1 = 1  
    fn = 1
    if n < 0:
        return -1
    elif n == 1 or n == 0:
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

print(fibonacci_1(10)) #55

#Cách 2:
def fibonacci_de_quy(n):
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print(fibonacci_de_quy(5)) #

#Cách 3: sử dụng numpy
import numpy as np
n = 20
a = (1 + np.sqrt(5))/2
b = (1 - np.sqrt(5))/2
Fn = (a**n - b**n)/(np.sqrt(5))
print(int(Fn)) #6765