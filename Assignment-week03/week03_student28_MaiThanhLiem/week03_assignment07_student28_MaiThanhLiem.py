import math

# using square root function of math module
n = 600851475143
prime_factor_of_n = []

for i in range(3, int(math.sqrt(n)) + 1, 2):
    # Because n is odd, we don't need to check for even number
    # The for loop only runs till square root of n, because if n has prime factors
    # then the least prime factor has to be less than square root of n
    if n % i == 0:
        prime_factor_of_n.append(i)
        n = n / i

# After the for loop, if n is prime itself, the list prime_factor_of_n will be empty
if n > 2:
    prime_factor_of_n.append(n)

print(max(prime_factor_of_n))
