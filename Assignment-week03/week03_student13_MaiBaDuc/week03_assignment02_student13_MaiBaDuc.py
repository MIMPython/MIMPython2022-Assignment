'''
Bai 2: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
s=0

with open('D://Python//demo.txt') as file_object: #luu 100 so trong file demo.txt
    for line in file_object:
        line = int(line)
        s += line

x = str(s)

x = tuple(x)

result = int(x[0])*10000 + int(x[1])*1000 + int(x[2])*100 + int(x[3])*10 + int(x[4])

print(result)



