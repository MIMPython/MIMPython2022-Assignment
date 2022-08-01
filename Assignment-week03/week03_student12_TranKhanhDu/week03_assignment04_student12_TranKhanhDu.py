#solution 1:
n = int(input("Enter a number: "))
if n == 0 or n == 1:
    print("Fibonacci number F"+ str(n) + " is:" + str(n))
else: 
    F0 = 0
    F1 = 1
    temp = 0
    fibonacci_number = F0 + F1
    if n == 2: 
        print("Fibonacci number F2 is:  " + str(fibonacci_number))
    else:
        for i in range(n - 2):
            temp = F1
            F0 = temp
            F1 = fibonacci_number
            fibonacci_number = F0 + F1
    #print to check fibonacci number
    print("Fibonacci number F" + str(n) +" is: " + str(fibonacci_number))
#sollution 2: 
#use numpy library to print Fibonacci sequence
import numpy as np
arr = np.array([4,4,4,4,4])
print(arr)


