with open("large_sum.txt", "r") as f:
    data = f.read().splitlines()  # data read as strings

sum = 0

for i in range(len(data)):
    sum += int(data[i])  # turn strings into integer numbers

print(str(sum)[:10])
# turn numbers into string and print 10 first letters of the string
