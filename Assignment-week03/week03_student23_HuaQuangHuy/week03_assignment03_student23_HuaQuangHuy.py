# Bài tập 3: 
# đọc dữ liệu từ file names.txt
with open('names.txt', 'r') as f:
    listNames = f.read().split(',')

# sort the list name 
listNames.sort()
listAlphabet = ['', 'A', 'B', 'C', 'D', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


total = 0
for i in range(0, len(listNames)):
    valueSpecial = 0
    for k in range(1, len(listNames[i]) - 1):
        # get sum of index each charactor in name from alphabet table
        valueSpecial += listAlphabet.index(listNames[i][k])

    # print(valueSpecial)
    total += (i + 1) * valueSpecial

print(total)  # 934389893
