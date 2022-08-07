import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def check(n,i):  
    while n%i !=0:
        i-=1
    if(prime(i)==1):
        return i
    else :
        return check(n,i-1)
n=int(input())
i=int(math.sqrt(n))
print(check(n,i))