import math
"""
Chương trình này hiện đang sai đề bài và do nhiều vấn đề chủ quan nên chưa hoàn thiện được!
"""
def C(n,k):
    if n==k:
        return 1
    return int(A(n,k)/gt(k,1))

def A(n,k):
    if n == k:
        return 1
    return gt(n,n-k+1)

def gt(f,l):
    f,l = max(f,l),min(f,l)
    muti = 1
    for i in range(f,l-1,-1):
        muti*=i
    return muti

def eratosthenes(n):
    prime = [True for i in range (n+1)]
    prime[0]=prime[1]=False
    for i in range(2,int(n**0.5)+1):
        if i:
            for j in range (i*i,n+1,i):
                prime[j] = False
    return prime.count(True)

# Probability of 2 prime numbers
def probabilityPrime(n):
    numberPrime = eratosthenes(n)
    return C(numberPrime,2)/C(n,2)

    

# Greatest common divisor
def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a>b:
        return gcd(a-b,b)
    elif(a<b):
        return gcd(a,b-a)
    return a

if __name__ == "__main__":
    n = int(input())
    print(probabilityPrime(n))
    print(2/math.pi**10)
