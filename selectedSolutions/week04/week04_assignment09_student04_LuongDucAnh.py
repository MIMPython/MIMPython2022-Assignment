#Function to count Trailing Zeros of a Factorial
def countTrailingZeros(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += n//i
        i *= 5
    return count

#Function to get last non Zero digit of a Factorial. How it works? Read at https://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
def getLastDigitNoTrailingZeros(n): #Function to get last non Zero digit of a Factorial. How it work
    digit = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8] #Last non-zero digit of factorial from 0 to 9
    if n < 10:
        return digit[n]
    if (((n//10)%10)%2 == 0): #check whether second last digit is odd or even
        return (6*getLastDigitNoTrailingZeros(n//5)*digit[n%10]) % 10
    else:
        return (4*getLastDigitNoTrailingZeros(n//5)*digit[n%10]) % 10

def main():
    n = 1000000
    print(countTrailingZeros(n)) #249998
    print(getLastDigitNoTrailingZeros(n)) #4

if __name__ == "__main__":
    main()