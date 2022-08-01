#funtion to check prime number
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#function to find max prime factor
def find_max_prime_factor(number):
    prime_factor = []
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factor.append(i)
    max_prime_factor = 0
    for ele in prime_factor:
        if ele > max_prime_factor:
            max_prime_factor = ele
    print(prime_factor)
    print("max prime factor of number " + str(number) + " is " + str(max_prime_factor))
find_max_prime_factor(600851475143)
#600851475143 is an enormous number too
    