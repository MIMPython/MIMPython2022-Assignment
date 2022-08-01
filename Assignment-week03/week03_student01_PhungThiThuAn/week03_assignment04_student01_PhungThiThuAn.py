# solution 1
def fibonacci_1(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)

print(fibonacci_1(6)) #8

# solution 2
import numpy as np
def fibonacci_2(n):
    temp = np.sqrt(5)
    alpha = (1 + temp)/2
    beta = (1 - temp)/2
    return np.round((np.power(alpha, n) - np.power(beta, n))/temp)

print(fibonacci_2(6))
