# Bài tập 7. (largest prime factor)

def eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    list_prime = []
    for i in range(2, n + 1):
        if prime[i] == True:
            list_prime.append(i)
    return list_prime


def prime_factor(n, list_prime):
    i = 0
    while n > 1:
        if n % list_prime[i] == 0:
            n /= list_prime[i]
        else:
            i += 1
    largest_prime = list_prime[i]
    return largest_prime


if __name__ == "__main__":
    prime_nums = eratosthenes(100000)
    print(prime_factor(13195, prime_nums))  # 29
    print(prime_factor(600851475143, prime_nums))  # 6857