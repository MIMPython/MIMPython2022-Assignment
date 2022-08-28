"""
Bài tập 1. (numpy)
"""

#a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều 
#   (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.

from array import array
import random

def two_dimension_array(m, n):
    array = []
    for i in range(0, m):
        row = []
        for j in range(0, n):
            row.append(random.randint(0, 10))
        array.append(row)
    return array
            
def two_dimension_array1(row, col):
    array = [[random.randint(0, 10) for i in range(col)] for j in range(row)]
    return array

arr = two_dimension_array1(3, 4)
print(arr)

# b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng 
# một cột của một bảng số cho trước.

def sumOfAColumn(array):
    sumColumns = []
    n = len(array[0])
    for i in range(len(array[0])):
        sumCol = sum(array[j][i] for j in range(len(array)))
        sumColumns.append(sumCol)
    return sumColumns

print(sumOfAColumn(arr))

# c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).

import numpy as np

arr = np.ndarray.randint(5, size = (3,4))