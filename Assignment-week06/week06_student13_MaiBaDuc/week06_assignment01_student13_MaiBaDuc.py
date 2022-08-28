'''
a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều (kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng một cột của một bảng số cho trước.
c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).
d) So sánh tốc độ thực hiện của hai hàm tính tổng các số theo cột đã cài đặt ở trên. Một số lưu ý:

Nên kiểm nghiệm kết quả trên những bảng số với kích thước lớn, đồng thời chạy chương trình nhiều lần để cho ra kết quả mang ý nghĩa 
thống kê.
Có thể sử dụng thư viện time để đo thời gian, cụ thể là dùng hàm time.time() hoặc time.perf_counter().
Cần so sánh tốc độ thực hiện chương trình trên những bộ dữ liệu đầu vào tương tự nhau.
Cần tách riêng thời gian tạo dữ liệu bảng số và thời gian tính tổng các số.
Nên thể hiện kết quả so sánh thông qua hình vẽ.
e) Trả lời câu hỏi tương tự cho việc tính tổng các số thuộc cùng một hàng của bảng số.'''


import random
import numpy as np
import time
# m = int(input("Số hàng: "))
# n = int(input('Số cột: '))
m=3
n=5

matrix = [ [0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        a = int(random.random()*10)
        matrix[i][j] = a

result = []
def sum_col_1():
    sum= 0
    for i in range(n):
        for j in range(m):
            sum += matrix[j][i]
        result.append(sum)
        sum = 0
    print(result)

mtr = np.random.randint(1,10,(m,n))
def sum_col_2():
    # mtr = np.ranint(1,9,(m,n))
    s = np.sum(mtr, axis=0)
    print(s)

time_1 = time.time()
sum_col_1()
print("--- %s seconds ---" % (time.time()*1000  - time_1*1000))
time_2 = time.time()
sum_col_2()
print("--- %s seconds ---" % (time.time()*1000  - time_2*1000))

def sum_row_1():
    sum = 0
    arr = []
    for i in range(m):
        for j in range(n):
            sum += matrix[i][j]
        arr.append(sum)
        sum = 0
    print(arr)

def sum_row_2():
    sum = np.sum(mtr, axis = 1)
    print(sum)
time_3 = time.time()
sum_col_1()
print("--- %s seconds ---" % (time.time()*1000  - time_3*1000))
time_4 = time.time()
sum_row_2()
print("--- %s seconds ---" % (time.time()*1000  - time_4*1000))
