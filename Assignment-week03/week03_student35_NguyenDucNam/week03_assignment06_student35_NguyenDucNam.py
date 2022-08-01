import random
import math
#Cau a
def max_divisor(a,b):
    if b == 0:
        return a
    return max_divisor(b,a%b)

#Cau b
def isPrime(a):
    if a == 1:
        return 1
    for x in range(2,math.sqrt(a)):
        if a % x == 0:
            return 0
            break
        return 1

count = 0
for i in range(0,100):
    random_1 = random.randint(1,10**6)
    random_2 = random.randint(1,10**6)
    if isPrime(random_1) == 1 and isPrime(random_2) == 1:
        count += 1
P = count / 100
