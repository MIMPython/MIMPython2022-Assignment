"""
Bài tập 2. (large sum)
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# """
def the_first_ten_digits(numbers):
    return str(sum(numbers))[ : 10]
   
path = 'data.txt'
with open(path, 'r') as file:
    numbers = file.read().splitlines()
numbers = [int(number) for number in numbers]

print (the_first_ten_digits(numbers))


