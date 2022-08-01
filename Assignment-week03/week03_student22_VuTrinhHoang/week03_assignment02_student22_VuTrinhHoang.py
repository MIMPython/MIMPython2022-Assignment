
data = 'B2.txt'
with open(data, 'r') as f:
    allLines = f.read().splitlines()
    # print(allLines)
tong = 0
# id=50
# while id>10:
#     for i in allLines:
#         tong+=int(i)%pow(10,51-id)/pow(10,50-id)
#     tong=int(tong/10)
#     id-=1
# for i in allLines:
#     tong=int(tong+int(i)/pow(10,52-id))
for i in allLines:
    tong+=int(i)
temp = tong
id = 0
while temp > 0:
    id+=1
    temp=int(temp/10)
print(int(tong/pow(10,id-10)))
f.close()
