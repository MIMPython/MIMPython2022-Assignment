from unittest import result

#tim so fibonacci thu n
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        x0 = 0
        x1 = 1
        xn = 0
        while n >= 2:
            xn = x0 + x1
            x0 = x1
            x1 = xn
            n -= 1
        return xn
n = -1
while n < 0:
    n = int(input("nhap vi tri so fibonacci: "))
    if n > 0:
        break
number = fibonacci(n)
print(number)