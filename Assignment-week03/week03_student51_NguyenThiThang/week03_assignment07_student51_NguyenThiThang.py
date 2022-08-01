def isPrime(x):
    for i in range(2,x):
        if (x % i == 0) :
            return False
    return True

def largestPrimeFactor(n):
    uoc=2
    while (n >1 ):
        while (n%uoc==0):
            n = n/uoc
        
        if (n==1):
            break

        uoc=uoc+1
        while (isPrime(uoc)==False):
            uoc=uoc+1

    return uoc

if __name__=='__main__':
    print("Uoc nguyen to lon nhat cua 600851475143 la:")
    print(largestPrimeFactor(600851475143)) #6857
   


