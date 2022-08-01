def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def largestPrimeFactor(x):
    prime_factors = []
    i = 2
    while x > 1:
        while x % i == 0:
            if isPrime(i):
                prime_factors.append(i)
            x = x/i
        i = i + 1
    return max(prime_factors)


print("The largest prime factor of the number 600851475143:",
      largestPrimeFactor(600851475143))  # The largest prime factor of the number 600851475143: 6857
