#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
a = 3710728753
sum = 0
while(a>0):
    sum+=a % 10
    a = a//10
print(sum)#43
