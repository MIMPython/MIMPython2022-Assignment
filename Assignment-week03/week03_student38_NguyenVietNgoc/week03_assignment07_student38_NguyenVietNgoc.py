def maxPrimeFactors(n):
    primeFactors = []
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
            primeFactors.append(i)
        i = i + 1

    primeFactors.append(int(n))
    print (primeFactors)

    return int(n)

if __name__ == "__main__":
	print (maxPrimeFactors(60))	# 5
	print (maxPrimeFactors(13195))	# 29
	print (maxPrimeFactors(600851475143))	# 6857
