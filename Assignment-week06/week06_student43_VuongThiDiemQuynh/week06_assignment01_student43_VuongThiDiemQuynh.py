'''
Bài tập 1. (numpy)
Mục tiêu của bài tập này là so sánh tốc độ thực hiện các phép toán tính tổng khi sử dụng thư viện numpy với khi sử dụng cách cài đặt thủ công. Dưới đây là danh sách gợi ý, không bắt buộc, những công việc cần thực hiện để giải quyết mục tiêu đề ra:
a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng một cột của một bảng số cho trước.

array = foo(3, 5)
array = [
  [2, 7, 3, 0, 0],
  [6, 4, 4, 3, 1],
  [0, 0, 9, 1, 2],
]
result = bar(array)
result = [8, 11, 16, 4, 3]
c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).
d) So sánh tốc độ thực hiện của hai hàm tính tổng các số theo cột đã cài đặt ở trên. Một số lưu ý:

Nên kiểm nghiệm kết quả trên những bảng số với kích thước lớn, đồng thời chạy chương trình nhiều lần để cho ra kết quả mang ý nghĩa thống kê.
Có thể sử dụng thư viện time để đo thời gian, cụ thể là dùng hàm time.time() hoặc time.perf_counter().
Cần so sánh tốc độ thực hiện chương trình trên những bộ dữ liệu đầu vào tương tự nhau.
Cần tách riêng thời gian tạo dữ liệu bảng số và thời gian tính tổng các số.
Nên thể hiện kết quả so sánh thông qua hình vẽ.
e) Trả lời câu hỏi tương tự cho việc tính tổng các số thuộc cùng một hàng của bảng số.
'''

import random
import numpy as np

# a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
def createArray(numberOfRow, numberOfColumn):
    array = []
    for i in range(numberOfRow):
        rowList = []
        for j in range(numberOfColumn):
            rowList.append(random.randint(1, 100))
        array.append(rowList)
    return array

# if __name__ == "__main__":
#     array = createArray(3, 5)
#     print(array)

# b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng một cột của một bảng số cho trước.
def sumColumn(array):
    sumList = []   
    for j in range(len(array[0])):
        sumColumn = 0
        for i in range(len(array)):    
            sumColumn += array[i][j]       
        sumList.append(sumColumn)
    return sumList

# a = [[22, 13, 30, 64, 54], [7, 9, 46, 7, 54], [29, 4, 84, 11, 58]]
# test = sumColumn(a)
# print(test) # [58, 26, 160, 82, 166]
    

# c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).

# Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
def createArrayWithNumpy(numberOfRow, numberOfColumn):
    # array = print(np.ndarray(shape=(numberOfRow,numberOfColumn), dtype=int))
    array = np.random.randint(100, size=(numberOfRow, numberOfColumn))
    return array

# Tính tổng các số thuộc cùng một cột của một bảng số cho trước.
'''
numpy.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
'''
def sumColumnWithNumpy(array):
    return np.sum(array, axis=0) # axis=0 => sum of columns; axis=1 => sum of rows

#=========TEST=========#

if __name__ == "__main__":
    array_a = createArray(3, 5)
    print(array_a)

    a = [[22, 13, 30, 64, 54], [7, 9, 46, 7, 54], [29, 4, 84, 11, 58]]
    sum_b = sumColumn(a)
    print(sum_b) # [58, 26, 160, 82, 166]

    array_c = createArrayWithNumpy(3, 5)
    print(array_c)

    sum_c = sumColumnWithNumpy(a)
    print(sum_c) # [58, 26, 160, 82, 166]

