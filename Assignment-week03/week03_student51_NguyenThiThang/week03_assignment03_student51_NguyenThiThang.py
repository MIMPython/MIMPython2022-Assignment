path = '.\Desktop\python\p022_names.txt'
with open(path,'r') as f:
    allNames = f.read().split(",")

allNames = sorted(allNames)

scoreNames = [0]*len(allNames)
for i in range(len(allNames)):
    for j in range(1,len(allNames[i])-1):
        scoreNames[i] += ord(allNames[i][j]) - 64
    scoreNames[i] =scoreNames[i] * (i+1)

print(allNames[937])
print(scoreNames[937]) # kiem tra vi du trong dau bai
print("Tong diem cac ten trong file la:")
print(sum(scoreNames))



