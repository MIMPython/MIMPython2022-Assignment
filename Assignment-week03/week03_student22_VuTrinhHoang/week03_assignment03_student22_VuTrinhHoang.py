
data = 'p022_names.txt'
def xet (s):
    tong = 0
    for i in s:
        tong+=ord(i)-ord('A')+1
        # print(i)
        # print(ord(i)) 
    return tong
        
with open(data, 'r') as f:
    allLines = f.read().split(',')
    # print(allLines)
    allLines.sort()
id=1
Tong=0
for i in allLines:
    # print(xet(i[1:len(i)-1])*id)
    Tong+=xet(i[1:len(i)-1])*id
    id+=1
    # xet(i)
print(Tong)