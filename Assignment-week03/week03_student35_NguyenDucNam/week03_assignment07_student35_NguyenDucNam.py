def max_prime(num):
    factor = 2 
    while factor * factor <= num:
        while num % factor == 0:
            num /= factor
        factor += 1
    if(num > 1):
        return num
    

def main():
    print(max_prime(600851475143))

main()