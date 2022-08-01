
# cách 1 (đệ quy)
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
print(fibonacci(20))#6765

#cách 2 ()
import numpy

def fib(n):
    return (numpy.matrix([[2, 1], [1, 1]]) ** (n // 2))[0, (n + 1) % 2]
print(fib(20))#6765

