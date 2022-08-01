f = open("names.txt",'r')
names = f.read()[1:-1].split('","')
names.sort()
print(names)

name = "GAYLA"
arr = []
for i in range(len(name)):
    arr.append(ord(name[i]) - ord('A') + 1)
print(arr) # [1, 12, 9, 3, 5]

count = 0
for i in range(len(names)):
    count +=1
    if(names == name):
        break;
print(sum(arr)*count) #154890


