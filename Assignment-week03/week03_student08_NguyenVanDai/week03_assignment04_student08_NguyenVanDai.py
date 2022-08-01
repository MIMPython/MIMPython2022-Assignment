#c1_dequy
def fibonaci_dequy(n):
    if (n<=1):
        return 1
    else:
        return (fibonaci_dequy(n-1)+fibonaci_dequy(n-2))
number = int(input('input number:'))
print('fibonaci:')
for i in range(number):
    print(fibonaci_dequy(i))
#c2-vong lap
def fibonaci_vonglap(n):
    f0=1
    print(f0)
    f1=1
    print(f1)
    for i in range(2,n+1):
        f=f0+f1
        print(f)
        f0=f1
        f1=f
number = int(input('input number:'))
fibonaci_vonglap(number)
# cách 3 : numpy 
import numpy as np

a = np.arange(1, 7)
length = len(a)
  
sqrtf = np.sqrt(5)
alpha = (1 + sqrtf) / 2
beta = (1 - sqrtf) / 2
  
fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtf))
print("The first {} numbers of Fibonacci series are {} . ".format(length, fn))
# c4: import sympy  
from sympy import * 
  
n = 5
print("Value of n = {}".format(n)) 
   
nth_fibonacci = fibonacci(n)   
      
print("Value of nth fibonacci number:{}".format(nth_fibonacci))