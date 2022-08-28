import numpy as np
from random import randint as rd
import time
import matplotlib.pyplot as plt

# a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
def create2DArray(m, n):
    array = []
    for i in range(m):
        array.append([rd(0, 1e10) for j in range(n)])
    return array

# b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng một cột của một bảng số cho trước.
def sumOfColumns(array):
    numCol = len(array[0])
    result = [0 for i in range(numCol)]
    for i in range(numCol):
        for j in range(len(array)):
            result[i] += array[j][i]
    return result
'''
array1 = create2DArray(2, 3)
print(array1)
result = sumOfColumns(array1)
print(result)
[[3, 9], [8, 1], [8, 10]]
[19, 20]
'''
# c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).
array2 = np.ndarray((2,3), int)
print(array2)
print(array2.sum(axis=0))

# d, So sánh 2 hàm tính tổng 2 số

# Tạo ra 1 mảng 2 chiều với kích thước lớn
array1 = create2DArray(10000, 1000)
array2 = np.asarray(array1)

path1 = './additionalFolder/compareInE1(part1).txt'
loop = 20

with open(path1, 'w') as f:
    f.write('Runtime of 2 function:\n')
    f.write('My function \t Numpy\n')
for i in range(loop):
    myFuncStartTime = time.time()
    result1 = sumOfColumns(array1)
    myFuncEndTime = time.time()
    myFuncRunTime = myFuncEndTime - myFuncStartTime

    npFuncStartTime = time.time()
    result2 = array2.sum(axis=0)
    npFuncEndTime = time.time()
    npFuncRunTime = npFuncEndTime - npFuncStartTime
    with open(path1, 'a') as f:
        f.write(f'{myFuncRunTime:.8f} \t {npFuncRunTime:.8f}\n')

data = open(path1, 'r')
data = data.read().splitlines()[2:]

myFunc = []
npFunc = []
for i in data:
    runtime = i.split(f' \t ')
    myFunc.append(float(runtime[0]))
    npFunc.append(float(runtime[1]))

times = list(range(loop))

plt.plot(times, myFunc, '--sr')
plt.plot(times, npFunc, '--sb')
plt.savefig('additionalFolder/plotCompareInE1(part1).jpg')
# plt.show()

# e) Trả lời câu hỏi tương tự cho việc tính tổng các số thuộc cùng một hàng của bảng số.
def sumOfRows(array):
    numRow = len(array)
    result = [0 for i in range(numRow)]
    for i in range(numRow):
        for j in range(len(array[0])):
            result[i] += array[i][j]
    return result
'''
array1 = create2DArray(2, 3)
print(array1) #[[7160044806, 5650258072, 2623093349], [2110065546, 3521035149, 4146079670]]
print(sumOfRows(array1)) # [15433396227, 9777180365]
array2 = np.asarray(array1)
print(np.sum(array2, axis=1)) # [15433396227  9777180365]
'''

path2 = './additionalFolder/compareInE1(part2).txt'

with open(path2, 'w') as f:
    f.write('Runtime of 2 function:\n')
    f.write('My function \t Numpy\n')
for i in range(loop):
    myFuncStartTime = time.time()
    result1 = sumOfRows(array1)
    myFuncEndTime = time.time()
    myFuncRunTime = myFuncEndTime - myFuncStartTime

    npFuncStartTime = time.time()
    result2 = array2.sum(axis=1)
    npFuncEndTime = time.time()
    npFuncRunTime = npFuncEndTime - npFuncStartTime
    with open(path2, 'a') as f:
        f.write(f'{myFuncRunTime:.8f} \t {npFuncRunTime:.8f}\n')

data = open(path2, 'r')
data = data.read().splitlines()[2:]

myFunc = []
npFunc = []
for i in data:
    time = i.split(f' \t ')
    myFunc.append(float(time[0]))
    npFunc.append(float(time[1]))

times = list(range(loop))

plt.plot(times, myFunc, '--sr')
plt.plot(times, npFunc, '--sb')
plt.savefig('additionalFolder/plotCompareInE1(part2).jpg')
# plt.show()

print('done')