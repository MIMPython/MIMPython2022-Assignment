file = open('LargeSum.txt', 'r')
data = file.read(10)
file.close()

for number in data:
    print(number)