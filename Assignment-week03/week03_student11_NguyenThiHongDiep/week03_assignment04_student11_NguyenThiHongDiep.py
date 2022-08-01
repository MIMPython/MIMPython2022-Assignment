# Cách 1
def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
    if (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
if __name__ == '__main__':
    print(fibonacci(1)) # 1
    print(fibonacci(6)) # 8
    print(fibonacci(23)) # 28657

# Cách 2
def fibonacci(n):
    if (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
if __name__ == '__main__':
    print(fibonacci(2)) # 1
    print(fibonacci(15)) # 610
    print(fibonacci(11)) # 89

# Cách 3

