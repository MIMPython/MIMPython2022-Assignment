import imp
from itertools import count


import math

def demBoi(x,n):
    t=math.pow(5,x)
    count=0
    for i in range(1,n+1):
        if (i % t ==0):
            count +=1
    return count

def demChuSo0(n):
    x=5
    mu=1
    s=0
    while(x<=n):
        s+=demBoi(mu,n)
        mu+=1
        x=math.pow(5,mu)
    return s

if __name__=='__main__':
    print("Nhap n")
    n = int(input())
    print("So chu so 0 o tan cung cua",n,"! la:")
    print(demChuSo0(n))