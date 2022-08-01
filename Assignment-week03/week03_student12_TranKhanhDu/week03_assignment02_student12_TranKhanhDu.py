from distutils.command.build_scripts import first_line_re
from traceback import print_exception


file_path = 'D:\\VisualCode\\Python\\MIM2022Python\\one-hundred_50digits_numbers.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
sum = 0
for line in lines:
    sum += int(line)
print(str(sum))
# firstly, print sum of 100 numbers, then we print 10 first digit numbers to prove that 
# the answer is true
first10digits = ""
for index in range(10):
    first10digits += (str(sum)[index])
print(first10digits)
