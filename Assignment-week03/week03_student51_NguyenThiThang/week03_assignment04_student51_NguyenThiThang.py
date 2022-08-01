import numpy as np

def fibonacci_cach1(n):
    arr=np.zeros(n,dtype=int)
    arr[0]=0
    arr[1]=1
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n-1]

def fibonacci_cach2(n):
    if (n<0):
        return -1
    elif (n==1 or n==2):
        return n-1
    else:
        return fibonacci_cach2(n-1) + fibonacci_cach2(n-2)
    

if __name__=='__main__':
    print("Nhap n")
    n=int (input())
    print(fibonacci_cach1(n))
    print(fibonacci_cach2(n))

