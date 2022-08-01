from code import interact
from tkinter.tix import INTEGER


def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == '__main__':
    x = float(input('enter number: '))
    print (fibonacci(x))
