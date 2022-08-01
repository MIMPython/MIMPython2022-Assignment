"""
Viết một chương trình tính số Fibonacci Fn với một số tự nhiên n cho trước.  
Hãy giải quyết bài tập này bằng nhiều cách khác nhau, trong đó có cách sử dụng  
thư viện numpy, sympy. 
"""
# Cách 1: Sử dùng thư viện numpy với Công thức Binet .

import numpy as np
# Tạo một mảng chứa n phần tử
# Để nhận được số fibonacci 'n' đầu tiên
fNumber = int(input("Enter the value of n+1'th number: "))
a = np.arange(1,fNumber)
length_a = len(a)

#Tính các điều kiện
sqrt_five = np.sqrt(5)
alpha = (1 + sqrt_five)/2
beta = (1 - sqrt_five)/2

#np.rint được dùng để làm tròn số nguyên 
Fn = np.rint(((alpha ** a) - (beta ** a))/ (sqrt_five))
print("The first {} numbers of Fibonacci series are {} " .format(length_a, Fn))

#Enter the value of n+1'th number: 10
#The first 9 numbers of Fibonacci series are [ 1.  1.  2.  3.  5.  8. 13. 21. 34.] 

# Cách 2: Sử dụng Sympy
from sympy import fibonacci
n = int(input())
print(fibonacci(n))
             