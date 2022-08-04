nameList = 'names.txt'
with open(nameList, 'r') as f:
    allLines = f.read().split(',')
    allLines.sort()

def xet (s):
    tong = 0
    for i in s:
        tong += ord(i) - ord('A') + 1
    return tong

id = 1
Tong = 0
for i in allLines:
    Tong += xet(i[1:len(i) - 1]) * id
    id += 1
print(Tong)
