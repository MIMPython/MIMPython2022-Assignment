from math import factorial


number = int(input("Enter a number: "))
factorial = 1
for element in range(1, number + 1):
    factorial *= element
print(str(factorial))
def find_number_of_number_zero(number):
    count = 0
    while number % 10 == 0:
        number = number / 10
        count += 1
    return "number of number zero: " + str(count)

def get_last_digit(number):
    while number % 10 == 0:
        number = number / 10
    return int(number % 10)


print(find_number_of_number_zero(factorial))
print(get_last_digit(factorial))
