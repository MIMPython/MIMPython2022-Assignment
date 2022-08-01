
#use recursion
def Fibonacci_recursion(n):
    if (n < 0):
        print("Invalid input")
    elif (n == 0):
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return Fibonacci_recursion (n-1) + Fibonacci_recursion (n-2)
    
#use numpy
#def Fibonacci_numpy(n):
#    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

print(Fibonacci_recursion(9))