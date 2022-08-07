#cách 1:
def fibonacci():
    n = int(input("Enter positive interger: "))
    f_0 = 0
    f_1 = 1
    for i in range(n - 1):
        f_n = f_0 + f_1
        f_0 = f_1
        f_1 = f_n
    print(f"Number Fibonacci F{n} is: {f_n}")
fibonacci()
#--------------------------------------------------------

#cách 2:
def fibonacci_1():
    n = int(input("Enter positive interger: "))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)   
print(fibonacci_1())
#---------------------------------------------------------

#cách 3:
import numpy as np
def fibonacci_2():
    n = int(input("Enter positive interger: "))
    f_n = ((((1 + np.sqrt(5)) / 2) ** n) - (((1 - np.sqrt(5)) / 2) ** n)) / (np.sqrt(5))
    print(f"Number Fibonacci F{n} is: {f_n:05f}")
fibonacci_2()