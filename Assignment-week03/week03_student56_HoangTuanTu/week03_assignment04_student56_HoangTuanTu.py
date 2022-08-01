import numpy
import sympy

# Read more at: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

# This method to check if user input unavailable value of n
def checkAvailable(n):
    if n == 1:
        print("The first {} numbers of Fibonacci series are {}" .format(n,1))
        return True
    elif n<=0:
        print("The first {} numbers of Fibonacci series are {}" .format(n,0))
        return True
    return False

# Print Result
def printArray(n,fibonacci):
    print("The first {} numbers of Fibonacci series are {}" .format(n,fibonacci))

def printNValue(n,fibonacci):
    print("Value of {}-th fibonacci number : {}".format(n,fibonacci))  

# Normal way: f(n) = f(n-1)+f(n-2)
def fNormal(n):
    if checkAvailable(n):
        return
    fibonacci = [1,1]
    for i in range (2,n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci
    

# Using Binet Fomuala in numpy 
# Read more at:
# + artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
# + geeksforgeeks.org/numpy-fibonacci-series-using-binet-formula
def fNumpy(n):
    if checkAvailable(n):
        return
    fibonacci = numpy.arange(1, n+1)
    sqrtFive =(n//2)**(1/2)
    alpha = (1 + sqrtFive) / 2
    beta = (1 - sqrtFive) / 2
    Fn = numpy.rint(((alpha ** fibonacci) - (beta ** fibonacci)) / (sqrtFive))
    return (Fn)

# Using fibonacci method in sympy
# Read more at: geeksforgeeks.org/python-sympy-fibonacci-method
def fSympy(n):
    return sympy.fibonacci(n)

# Using Dynamic Programming
# Read more at: towardsdatascience.com/dynamic-programming-i-python-8b20387870f5
def F_memo(n, memo):
	if n == 1 or n == 2:
		return 1
	if not memo[n] == None:
		return memo[n]
	result = F_memo(n - 1, memo) + F_memo(n - 2, memo)
	memo[n] = result
	return result

def fDynamicProgramming(n):
	memo = [None] * (n + 1) # create a list have n + 1 element have value None
	return F_memo(n, memo)

# main method
if __name__ == "__main__":
    n = int(input("Input number n: "))

    print("Using normal way: ")
    printArray(n,fNormal(n))
    print()
    
    print("Using Numpy way: ")
    printArray(n,fNumpy(n))
    print()

    print("Using Sympy way: ")
    printNValue(n,fSympy(n))
    print()

    print("Using Dynamic Programming way: ")
    printNValue(n,fDynamicProgramming(n))
    print()

    
