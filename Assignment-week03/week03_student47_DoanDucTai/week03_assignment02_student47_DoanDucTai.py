#bài 2. Work out the first ten digits of the sum of the following 
# one-hundred 50-digit numbers
#data.txt chứa input

from re import A
from tokenize import String


path ="data.txt"
with open(path, 'r') as f:
    allLines = f.read().splitlines() 
sum = 0
for i in allLines:
    sum += int(i)
string_sum = str( sum )
print(string_sum[0:9])