# import time

def collatzSeq(num, dict):
    length = 1
    oriNum = num
    while num > 1:
        if num < oriNum:
            length += dict[num] - 1
            break
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        length += 1
    dict[oriNum] = length
    return dict
   
result = {}

# start = time.time()
for i in range (1, 1000000):
    result = collatzSeq(i, result)
# print(time.time() - start)

keyList = list(result.keys())
valList = list(result.values())
maxSeqLen = max(valList)

print(keyList[valList.index(maxSeqLen)])