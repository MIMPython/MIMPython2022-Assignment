import time
import numpy as np
# Bài 2:

def mean_array_non_numpy(array):
    try:
        size_array = len(array) * len(array[0])
        sum_array = 0
        for row in range(len(array)):
            for column in range(len(array[0])):
                sum_array += array[row][column]
        return sum_array / size_array
    except Exception:
       print("Không có phần tử nào trong mảng số.")

def median_array_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        list_element_in_array.sort()
        if len(list_element_in_array) % 2 == 0:
            return list_element_in_array[int(len(list_element_in_array) / 2)]
        else:
            middle_element_1 = len(list_element_in_array) // 2  
            middle_element_2 = len(list_element_in_array) // 2 + 1
            result = (list_element_in_array[middle_element_1] + list_element_in_array[middle_element_2])/ 2
            return result
    except IndexError:
        print("Không có phần tử nào trong mảng số.")

def median_array_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        list_element_in_array.sort()
        if len(list_element_in_array) % 2 == 0:
            return list_element_in_array[int(len(list_element_in_array) / 2)]
        else:
            middle_element_1 = len(list_element_in_array) // 2  
            middle_element_2 = len(list_element_in_array) // 2 + 1
            result = (list_element_in_array[middle_element_1] + list_element_in_array[middle_element_2])/ 2
            return result
    except IndexError:
        print("Không có phần tử nào trong mảng số.")


def max_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        list_element_in_array.sort()
        return list_element_in_array[- 1]
    except IndexError:
        print("Không có phần tử nào trong mảng số.")


def min_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        list_element_in_array.sort()
        return list_element_in_array[0]
    except IndexError:
        print("Không có phần tử nào trong mảng số.")


def argmax_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        for index in range(len(list_element_in_array)):
            if list_element_in_array[index] == max(list_element_in_array):
                return index
    except IndexError:
        print("Không có phần tử nào trong mảng số.")

def argmin_non_numpy(array):
    try:
        list_element_in_array = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                list_element_in_array.append(array[row][column])
        for index in range(len(list_element_in_array)):
            if list_element_in_array[index] == min(list_element_in_array):
                return index
    except IndexError:
        print("Không có phần tử nào trong mảng số.")

def linspace_non_numpy(start, end, number_of_elements = 50):
    list_numbers = []
    if start >= end:
        distance = (start - end) / (number_of_elements - 1)
        for t in range(0 , number_of_elements ):
            element = start - t * distance
            list_numbers.append(element)
    else:
        distance = (end - start) / (number_of_elements - 1)
        for t in range(0 , number_of_elements ):
            element = start + t * distance
            list_numbers.append(element)
    return np.array(list_numbers)

def repeat_non_numpy(array, *args, **kwargs):
    if type(args[0]) == int:
            new_array = []
            for row in range(len(array)):
                for column in range(len(array[0])):   
                    for i in range(args[0]):
                        new_array.append(array[row][column])
            return np.array(new_array)
    for key, value in kwargs.items():
        if type(args[0]) == int and kwargs[key] == 0:
            new_array = []
            for row in range(len(array)):
                for i in range(args[0]):
                    new_array.append(array[row])
            return np.array(new_array)

        elif type(args[0]) == int and kwargs[key] == 1:
            new_array = []
            for row in range(len(array)):
                new_array_0 = []
                for column in range(len(array[0])):
                    for i in range(args[0]):
                        new_array_0.append(array[row][column])
                new_array.append(new_array_0) 
            return np.array(new_array)

        
        
        elif len(args) == 1:
            if len(args) == 1 and kwargs[key] == 0:
                new_array = []
                for row in range(len(array)):
                    for i in range(len(args[0])):
                        if i == row:
                            for j in range(args[0][i]):
                                new_array.append(array[row])
                return np.array(new_array)
            elif len(args) == 1 and kwargs[key] == 1:
                new_array = []
                for row in range(len(array)):
                    new_array_0 = []
                    for column in range(len(array[0])):
                        for i in range(len(args[0])):
                            if i == column:
                                for j in range(args[0][i]):
                                    new_array_0.append(array[row][column])
                    new_array.append(new_array_0) 
                return np.array(new_array)
    

list_name = []
list_time_non_numpy = []
list_time_numpy = []

# - mean
"""
Hàm mean để tính trung bình cộng các phần tử nào đó.VD: dãy số = 1, 5, 4, 12, 8, 21, 4, 2.Thì có
mean = (1 + 5 + 4 + 12 + 8 + 21 + 4 + 2) / 8 = 7.125 (Trong đó 8 là số phần tử của dãy số)."""
# VD:

array = np.random.randint(0, 100, (1000, 1000))

start_1 = time.time()
mean_of_array = np.mean(array)
end_1 = time.time()

start_2 = time.time()
mean_array_non_numpy(array)
end_2 = time.time()

list_name.append('mean')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

       
# - median 
"""
Median: được tính bằng cách sắp xếp các phần tử từ bé đến lớn, kết quả là số ở chính giữa, 
nếu có 2 số như vậy thì kết quả sẽ là trung bình cộng của 2 số đó. 

VD: mảng số = [[ 4,  2,  6],
               [ 1,  8, 49],
               [32, 23, 43],
               [ 6,  8,  9],
               [ 9,  9,  7]]

sắp xếp mảng số sau sắp xếp là 1, 2, 4, 6, 6, 7, 8, 8, 9, 9, 9, 23, 32, 43, 49
vậy meadian của dãy số trên là 8

VD: dãy số thứ 2= [[ 4,  2,  6], 
                   [ 8, 32, 23], 
                   [43,  6,  8], 
                   [ 9,  9,  9]]
dãy số sau sắp xếp là 1, 2, 4, 6, 6, 8, 8, 9, 9, 9, 23, 32, 43, 49
vậy meadian của dãy số trên là 8.5
"""

array = np.random.randint(0, 100, (1000, 1000))

start_1 = time.time()
median_of_array = np.median(array)
end_1 = time.time()

start_2 = time.time()
median_array_non_numpy(array)
end_2 = time.time()

list_name.append('median')

list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - max 
"""
Max: là giá trị lớn nhất  
VD: mảng số = [[ 4,  2,  6],
               [ 1,  8, 49],
               [32, 23, 43],
               [ 6,  8,  9],
               [ 9,  9,  7]]
vậy max là 43
"""
array = np.random.randint(0, 100, (1000, 1000))

start_1 = time.time()
max_of_array = np.max(array)
end_1 = time.time()

start_2 = time.time()
max_non_numpy(array)
end_2 = time.time()

list_name.append('max')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - min 
"""
Min: là giá trị nhỏ nhất  
VD: mảng số = [[ 4,  2,  6],
               [ 1,  8, 49],
               [32, 23, 43],
               [ 6,  8,  9],
               [ 9,  9,  7]]
vậy min là 2
# """
array = np.random.randint(0, 100, (1000, 1000))

start_1 = time.time()
min_of_array = np.min(array)
end_1 = time.time()

start_2 = time.time()
min_non_numpy(array)
end_2 = time.time()

list_name.append('min')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# -argmax
"""
argmax: trả về vị trí đầu tiên của giá trị lớn nhất
"""

array = np.random.randint(0, 100, (1000, 1000))

start_1 = time.time()
index_of_max_in_array = np.argmax(array)
end_1 = time.time()

start_2 = time.time()
argmax_non_numpy(array)
end_2 = time.time()


list_name.append('argmax')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - argmin
"""
argmin: trả về vị trí đầu tiên của giá trị nhỏ nhất
"""

array = np.random.randint(0, 100, (1000, 1000))
start_1 = time.time()
index_of_min_in_array = np.argmin(array)
end_1 = time.time()

start_2 = time.time()
argmin_non_numpy(array)
end_2 = time.time()

list_name.append('argmin')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - linspace 
"""
Trả về 1 mảng array 1 chiều với các phần tử cách đều nhau trong 1 khoảng nào đó
VD: np.linspace(0, 1, 5) 
Trong đó: Bắt đầu: 0, kết thúc: 1, số phần tử: 5
kết quả -> [0, 0.25, 0.5, 0.75, 1]

VD: np.linspace(2, 0, 8)
Trong đó: Bắt đầu: 2, kết thúc: 0, số phần tử: 8
kết quả: [2.         1.71428571 1.42857143 1.14285714 0.85714286 0.57142857 0.28571429 0.        ]

"""
start_1 = time.time()
np.linspace(2000, 60000, 30000)
end_1 = time.time()

start_2 = time.time()
np.linspace(2000, 60000, 30000)
end_2 = time.time()

list_name.append('linspace')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - arange 
"""
Trả về 1 mảng array 1 chiều với các phần tử cách đều nhau trong 1 khoảng nào đó

VD: np.arange(2, 11, 2) 
Trong đó: Bắt đầu: 2, kết thúc: 11, các phần tử cách nhau: 2
(ta sẽ lấy số gần nhất và bé hơn số kết thúc(11) chứ không lấy số kết thúc (11) thỏa mãn yêu cầu)
kết quả -> [2, 4, 6, 8, 10]

VD: np.arange(2, 0, 0.2)
Trong đó: Bắt đầu: 2, kết thúc: 0, các phần tử cách nhau 0.2
kết quả: []

VD: np.arange(0, 10, 15)
Trong đó: Bắt đầu: 0, kết thúc: 10, các phần tử cách nhau 15
kết quả: [0]
"""
start_1 = time.time()
np.arange(0, 1000000, 3)
end_1 = time.time()

start_2 = time.time()
[i for i in range(0, 1000000, 3)]
end_2 = time.time()

list_name.append('arange')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)

# - repeat
"""
Trả về array có shape giống với input trừ khi ta thêm các tham số đầu vào là axis


VD:
np.repeat(3, 4)
Kết quả -> array([3, 3, 3, 3])

x = np.array([[1,2],[3,4]])
np.repeat(x, 2)
Kết quả -> array([1, 1, 2, 2, 3, 3, 4, 4])

np.repeat(x, 3, axis=1)
Kết quả -> array([[1, 1, 1, 2, 2, 2],
                  [3, 3, 3, 4, 4, 4]])

np.repeat(x, [1, 2], axis=0)
Kết quả -> array([[1, 2],
                  [3, 4],
                  [3, 4]])
"""

array = np.random.randint(1, 100, size = (20, 30))
start_1 = time.time()
np.repeat(array, 2)
end_1 = time.time()

start_2 = time.time()
repeat_non_numpy(array, 2)
end_2 = time.time()

list_name.append('repeat')
list_time_non_numpy.append(end_2 - start_2)
list_time_numpy.append(end_1 - start_1)


# - ones
"""
Tạo ra 1 mảng với tất cả phần tử là 1
VD:array = np.ones((3,4))
Kết quả -> [[1. 1. 1. 1.]
            [1. 1. 1. 1.]
            [1. 1. 1. 1.]]
VD: array = np.ones((3,4), dtype = int)
Kết quả -> [[1 1 1 1]
            [1 1 1 1]
            [1 1 1 1]]
"""

start_1 = time.time()
array = np.ones((300, 400), dtype = int)
end_1 = time.time()

list_name.append('ones')
list_time_non_numpy.append(0)
list_time_numpy.append(end_1 - start_1)


# - zeros
"""
Tạo ra 1 mảng với tất cả phần tử là 0
VD:array = np.ones((3,4))
Kết quả -> [[0. 0. 0. 0.]
            [0. 0. 0. 0.]
            [0. 0. 0. 0.]]
VD: array = np.ones((3,4), dtype = int)
Kết quả -> [[0 0 0 0] 
            [0 0 0 0] 
            [0 0 0 0]]
"""
start_1 = time.time()
array = np.zeros((300, 400), dtype = int)
end_1 = time.time()

list_name.append('zeros')
list_time_non_numpy.append(0)
list_time_numpy.append(end_1 - start_1)



# - savetxt
"""
np.savetxt(file_name, X, delimiter=' ', newline='\n')
Trong đó,
1) file_name là tên file mà bạn muốn ghi  
2) X là dữ liệu mà bạn muốn lưu có kiểu là 1D hoặc 2D array
3) delimiter là chuỗi, kí tự bạn muốn chia cắt các cột
4) newline là chuỗi kí tự bạn muốn chia cắt các dòng
"""
x =np.random.randint(0, 10, [4, 7]) 
np.savetxt("text.txt", x, delimiter = "#", newline = "\n\n")

# - loadtxt
"""
numpy.loadtxt(file_name, dtype = float, delimiter = None)
Trogn đó,
1) file_name là tên file mà bạn muốn đọc
2) dtype là kiểu dữ liệu muốn 
3) delimiter là chuỗi, kí tự bạn muốn chia cắt các cột
Nếu kiểu dữ liệu có cấu trúc data-type, mỗi hàng sẽ được hiểu là 1 phần tử của mảng.
"""
np.loadtxt("text.txt", dtype = float, delimiter = ",")

# - apply_along_axis
"""
np.apply_along_axis(func, axis, arrary)
Trong đó,
1) func: là 1 hàm nào đó nhận vào mảng 1 chiều và nó được áp dụng cho việc loại bỏ trục 
được chỉ định 
2) axis = 1 theo cột, axis = 0 theo hàng
3)arrary: dữ liệu cần thực hiện
Trả về 1 mảng đầu ra có shape giống với array ngoại trừ trục bị loại bỏ
Trục này bị loại bỏ và được thay thế bởi  giá trị trả về của func vì thế giá trị 
trả về có thể có số chiều bé hơn array.
"""
# VD:
def my_func(a):
    return (a[0] + a[-1]) * 0.5

b = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.apply_along_axis(my_func, 0, b) # array([4., 5., 6.])
np.apply_along_axis(my_func, 1, b) # array([2.,  5.,  8.]) 



# - where
"""
numpy.where(condition, [x, y, ])
Trong đó,
1) condition, là 1 điều kiện nào đó
2) x, y là các broadcast
Trả về mảng có các phần tử từ x nếu đk là đúng, và các phần tử còn lại từ y.
"""
a = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])
np.where(a < 4, a, -1) # array([[ 0,  1,  2],
                       #        [ 0,  2, -1],
                       #        [ 0,  3, -1]])
       
a = np.where([[True, False], [True, True]],  # [[1 8]
         [[1, 2], [3, 4]],                   #  [3 4]]
         [[9, 8], [7, 6]])



# - argwhere
"""
numpy.argwhere(condition)
Trong đó,
1) condition, là 1 điều kiện nào đó.
Trả về mảng các vị trí thỏa mãn điều kiện.
"""
x = np.arange(6).reshape(2,3)           # array([[0, 1, 2],
                                        #        [3, 4, 5]])

np.argwhere(x>1)        # array([[0, 2],
                        #        [1, 0],
                        #        [1, 1],
                        #        [1, 2]])

# - diag
"""
numpy.diag(arr [, k])
Nếu arr là mảng 2 chiều trả về ndarray là đường chéo thứ k (mặc định là 0) của arr đó
Nếu arr là mảng 1 chiều thì trả về mảng 2 chiều với arr có đường chéo thứ k là arr
"""
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.diag(b)  #[1 5 9]

b = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.diag(b)  # [[1 0 0]
            #  [0 2 0]
            #  [0 0 3]]

np.diag(b, k = - 1) # [[0 0 0 0]
                    #  [1 0 0 0]
                    #  [0 2 0 0]
                    #  [0 0 3 0]]

if __name__ == "__main__":
    print("-" * 73)
    print("|{: <11s}".format("Name function"), "|{: <21s}".format("Time for function non numpy"), \
        "|{: <21s}".format("Time for function by numpy"), "|")
    print("-" * 73)
    for i in range(len(list_time_numpy)):
        print("|{: <13s}".format(list_name[i]), "|{: <27f}".format(list_time_non_numpy[i]), \
            "|{: <26f}".format(list_time_numpy[i]), "|")
    print("-" * 73)
    