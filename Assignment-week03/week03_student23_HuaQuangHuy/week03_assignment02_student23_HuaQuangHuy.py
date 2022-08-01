# Bài tập 2: lấy 10 chữ số của tổng 100 số 50 chữ số
with open('data.txt', 'r') as f:
    listNumber = f.read().splitlines() # read value each line of file

# save value each file into new list, and convert them to float
finalList = []
for element in listNumber:
    finalList.append(float(element))

sum = 0
# sum of all element
for element in finalList:
    sum += element

first10Digits = sum
# get first 10 digits
while first10Digits > 10 ** 10:
    first10Digits = first10Digits // 10

print(first10Digits)  # 5537376230.0
