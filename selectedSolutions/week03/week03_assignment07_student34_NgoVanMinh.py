import math
def isPrime(n: int):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def solution_1(n: int):
    result = []
    for i in range(2,n):
        while n % i == 0 and isPrime(i):
            n = n / i
            result.append(i)
    print(max(result))

def solution_2(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n
if __name__ == '__main__':
    print(solution_1(13195))    #rất chậm
    print(solution_2(600851475143)) #nhanh hơn rất nhiều

