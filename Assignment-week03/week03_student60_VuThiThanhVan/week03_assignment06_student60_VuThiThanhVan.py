
def __gcd(a,b):
    while (a!=b):
        if a>b:
            a=a-b
        else :
            b=b-a
    return a
n=int(input())
m=int(input())

print(__gcd(n,m))