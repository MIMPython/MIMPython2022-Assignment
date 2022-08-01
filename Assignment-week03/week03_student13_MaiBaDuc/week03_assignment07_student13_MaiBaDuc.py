from cmath import sqrt
def isprime(x):
    for i in range(2,int(sqrt(x).real)+1):
        if x%i==0: return False
    return True
def func(x):
    lst = []
    for i in range(2,int(sqrt(x).real)+1):
        if (x%i==0) and (isprime(i)==True):
            if isprime(int(x/i))==True:
                lst.append(int(x/i))
            else: 
                lst.append(i)
    return lst

print(max(func(600851475143)))

