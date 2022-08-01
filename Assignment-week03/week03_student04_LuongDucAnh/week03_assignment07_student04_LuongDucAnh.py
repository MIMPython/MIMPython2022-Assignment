import math
        
def findPrimeFactors(n):
    listPrimeFactors = []
    while n % 2 == 0:
        n = n/2
        listPrimeFactors.append(2)
    for i in range (3, int(n/2) + 1, 2):
        if n <= 1:
            break
        while n % i == 0:
            n = n/i
            listPrimeFactors.append(i)
    if len(listPrimeFactors) == 0:
        listPrimeFactors.append(n)
    return listPrimeFactors

print (max(findPrimeFactors(600851475143)))