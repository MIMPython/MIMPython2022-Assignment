def fibo(n: int):
    f = [0, 1]
    [f.append(f[-1] + f[-2]) for i in range(n-1)]
    return f

fibo5 = fibo(5)
print(fibo5[4])     # 3
print(fibo5[5])     # 5
