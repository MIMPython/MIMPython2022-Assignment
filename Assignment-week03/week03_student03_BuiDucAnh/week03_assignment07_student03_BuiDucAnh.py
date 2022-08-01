#Phân tích số ra thừa số nguyên tố
def prime_factorization(number):
    i = 2
    listPrime = []
    while number > 1:
        if number% i == 0:
            number = int(number / i)
            listPrime.append(i)
        else:
            i += 1
    if len(listPrime) == 0:
        listPrime.append(number)
    return listPrime

listPrime = prime_factorization(600851475143)
length = len(listPrime)
maxPrime = listPrime[length - 1]
print(maxPrime)