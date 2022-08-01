# Bài tập 4: Tính số Fibonaci Fn
# Solution 1: recursive
def getFibonaci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return getFibonaci(n - 1) + getFibonaci(n - 2)

# solution 2: loop:


def getFibonacciByLoop(n):
    if n == 0 or n == 1:
        return 1
    f0 = 1
    f1 = 1
    f2 = f0 + f1
    i = 3
    while i <= n:
        f0 = f1
        f1 = f2
        f2 = f0 + f1
        i = i + 1
    return f2


if __name__ == "__main__":
    for i in range(6):
        print(getFibonacciByLoop(i))
