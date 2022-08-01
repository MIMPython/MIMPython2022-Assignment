import math
#Sử dụng công thức truy hồi đã tìm được về mặt lý thuyết
def Fibonacci(n):
    S = 0
    for i in range(1, n + 1):
        if i%2 == 1:
            S += math.comb(n,i)*5**((i-1)/2)
    return(S/2**(n-1))

