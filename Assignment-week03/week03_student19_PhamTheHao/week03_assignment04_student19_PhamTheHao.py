"""
Bài tập 4. (Fibonacci numbers)
F_0 = 0, F_1 = 1, F_n+2 = F_n+1 + F_n, n≥0
Viết một chương trình tính số Fibonacci Fn với một số tự nhiên n cho trước. Hãy giải quyết 
bài tập này bằng nhiều cách khác nhau, trong đó có cách sử dụng thư viện numpy, sympy.

"""
# Cach 1:
def fibonacci(n):
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f

print(fibonacci(7)) #f(7) = 13
print(fibonacci(9)) #f(9) = 34

# Cach 2:
import numpy as np
n = 9
arr = np.arange(1, n)
a = (1 + np.sqrt(5)) / 2
b = (1 - np.sqrt(5)) / 2
fn = np.rint(((a ** n) - (b ** n)) / (np.sqrt(5)))
print(fn)

