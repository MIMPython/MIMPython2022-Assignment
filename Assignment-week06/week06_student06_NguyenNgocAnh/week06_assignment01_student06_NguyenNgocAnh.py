"""
Bài tập 1. (numpy)
Mục tiêu của bài tập này là so sánh tốc độ thực hiện các phép toán tính tổng 
khi sử dụng thư viện numpy với khi sử dụng cách cài đặt thủ công. Dưới đây 
là danh sách gợi ý, không bắt buộc, những công việc cần thực hiện để giải 
quyết mục tiêu đề ra:
a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều 
(kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.
b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các 
số thuộc cùng một cột của một bảng số cho trước.

array = foo(3, 5)
array = [
  [2, 7, 3, 0, 0],
  [6, 4, 4, 3, 1],
  [0, 0, 9, 1, 2],
]
result = bar(array)
result = [8, 11, 16, 4, 3]
c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai 
ý (a) và (b).
d) So sánh tốc độ thực hiện của hai hàm tính tổng các số theo cột đã cài 
đặt ở trên. Một số lưu ý:

Nên kiểm nghiệm kết quả trên những bảng số với kích thước lớn, đồng thời 
chạy chương trình nhiều lần để cho ra kết quả mang ý nghĩa thống kê.
Có thể sử dụng thư viện time để đo thời gian, cụ thể là dùng hàm time.time() 
hoặc time.perf_counter().
Cần so sánh tốc độ thực hiện chương trình trên những bộ dữ liệu đầu vào tương tự nhau.
Cần tách riêng thời gian tạo dữ liệu bảng số và thời gian tính tổng các số.
Nên thể hiện kết quả so sánh thông qua hình vẽ.
e) Trả lời câu hỏi tương tự cho việc tính tổng các số thuộc cùng một hàng của bảng số.
"""
from random import randint
from time import perf_counter
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Tạo ma trận list
def create_matrix(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randint(0, 10)) 

        mat.append(row)
    return mat


# Tổng ma trận
def sum_colum(matrix):
    sum_by_colum = []
    for j in range(len(matrix[0])):
        sum = 0
        for i in range(len(matrix)):
            sum += matrix[i][j]
        sum_by_colum.append(sum)
    return sum_by_colum

# In ma trận list
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


# Thời gian tạo ma trận
def check_time_create_matrix(path_file):
    df = pd.read_csv(path_file)
    #print(df.sort_values(by=['ROW', 'COLUMN']))
    list_mul = []
    for i in range(len(df)):
        list_mul.append(df.ROW[i]*df.COLUMN[i])
    df_with_mul = pd.DataFrame({'ROW':df.ROW, 'COLUMN': df.COLUMN, 'MULTIPLY' : list_mul})
    df_with_mul = df_with_mul.sort_values(by=['MULTIPLY', 'COLUMN'])

    #so sánh thời gian
    list_time_list = []
    list_time_numpy = []
    for i in range(len(df_with_mul)):
        matrix = np.random.randint(0,10,size=(df_with_mul.ROW[i],df_with_mul.COLUMN[i]))
        # list
        time_list_start = perf_counter()
        sum_colum(matrix)
        time_list_end = perf_counter()
        list_time_list.append(time_list_end-time_list_start)

        #numpy
        time_numpy_start = perf_counter()
        np.sum(matrix, axis=0)
        time_numpy_end = perf_counter()
        list_time_numpy.append(time_numpy_end-time_numpy_start)


    df_time = pd.DataFrame({'MULTIPLY': df_with_mul.MULTIPLY, 'TIMELIST': list_time_list, 'TIMENUMPY': list_time_numpy})
    df_time.to_csv('additionalFolder/week06_assignment01_student06_NguyenNgocAnh_output.csv')
    
    #hình vẽ
    plt.figure(figsize=(15, 10))
    plt.scatter(df_time.MULTIPLY, df_time.TIMELIST, color='blue', label='LIST')
    plt.scatter(df_time.MULTIPLY, df_time.TIMENUMPY, color='red', label='NUMPY')
    plt.xlabel('kích thước ma trận', fontsize=14)
    plt.ylabel('thời gian', fontsize=14)
    plt.title('so sánh thời gian cộng theo cột ma trận', fontsize=18)
    plt.legend(fontsize=14)
    plt.grid()
    plt.show()


#tạo file test
"""
def gen_test():
    df = pd.DataFrame(np.random.randint(1,1001,size=(1000,2)),columns=['ROW', 'COLUMN'])
    df.to_csv("additionalFolder/week06_assignment01_student06_NguyenNgocAnh_test.csv")
"""


if __name__ == '__main__':
    matrix_list = create_matrix(3, 5)
    print_matrix(matrix_list)
    sum_colum_list = sum_colum(matrix_list)
    print(sum_colum_list)

    arr = np.random.randint(0,10,size=(3,5))
    print(arr)
    print(np.sum(arr, axis=0))
    #gen_test()
    path_file = "additionalFolder/week06_assignment01_student06_NguyenNgocAnh_test.csv"
    check_time_create_matrix(path_file)
    
