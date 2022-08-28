'''
Bài tập 2. (numpy methods)
Một số hàm trong thư viện numpy được liệt kê dưới đây.

- mean, median
- max, min
- argmax, argmin
- linspace, arange
- repeat, random
- all, any
- ones, zeros
- savetxt, loadtxt
- apply_along_axis
- where
- isclose
- polyfit, polyval
- roots
Hãy tìm hiểu một số hàm trong thư viện numpy (không nhất thiết thuộc danh sách trên) 
và thực hiện những yêu cầu sau:

Nêu ý nghĩa của hàm, cho ví dụ.
Viết chương trình thực hiện đúng ý nghĩa đó mà hạn chế sử dụng thư viện numpy. 
Có thể sử dụng thư viện để khởi tạo mảng số nếu cần thiết.
So sánh tốc độ thực thi giữa hai cách làm: phương pháp thủ công và phương pháp sử dụng numpy.'''

import numpy as np
import time


arr = np.random.randint(10,size=10)

# mean: giá trị trung bình của mảng
def mean_1():
    s = 0
    for i in arr: s += i
    return s/len(arr)
def mean_2():
    return np.mean(arr) #numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)

# time_mean_1 = time.time()
# mean_1()
# print(time.time()*1000-time_mean_1*1000)
# time_mean_2 = time.time()
# mean_2()
# print(time.time()*1000-time_mean_2*1000)

# median: giá trị trung vị
def median_1():
    arr.sort()
    if(len(arr) %2 == 0): return (arr[int(len(arr)/2)-1] + arr[int(len(arr)/2)])/2
    else: return arr[int(len(arr)/2)+1]
def median_2():
    return np.median(arr)

# time_median_1 = time.time()
# median_1()
# print(time.time()*1000-time_median_1*1000)
# time_median_2 = time.time()
# median_2()
# print(time.time()*1000-time_median_2*1000)

# argmax: trả về chỉ số của phần tử lớn nhất đầu tiên trong mảng

mtr = np.random.randint(1,10,(2,5))
def argmax_1(mtr):
    m = 0
    arr = []
    for i in mtr: 
        if max(i)>m: m = max(i)
    for i in mtr:
        for j in i: arr.append(j)
    for i in arr:
        if i==m: return arr.index(i)
def argmax_2():
    return np.argmax(mtr)
time_argmax_1 =  time.time()
argmax_1(mtr)
print(time.time()*10**6-time_argmax_1*10**6)
time_argmax_2 = time.time()
argmax_2()
print(time.time()*10**6-time_argmax_2*10**6)

# linspace:  tạo các giá trị có khoảng cách đều 
def linspace(start, end, quantity) :
    arr = []
    # if start is None: arr.append(0)
    # else: arr.append(start)
    num = start
    step = int((end-start)/(quantity-1))
    # if step is None: step = 1
    # else: step = step
    while(num <= end):
        arr.append(num)
        num += step
    return arr
def linspace_np(): 
    return np.linspace(1,5,3)
# time_linspace = time.time()
# linspace(1,5,3)
# print(time.time()*1000-time_linspace*1000)
# time_linspace_np = time.time()
# linspace_np()
# print(time.time()*1000-time_linspace_np*1000)

#repeat:  trả về mảng với các phần tử được lặp lại số lần nhất định
def repeat(number, rep):
    i = 0
    arr = []
    while i<rep:
        arr.append(number)
        i += 1
    return arr
def repeat_np():
    return np.repeat(3,5)
time_repeat = time.time()
repeat(3,5)
print(time.time()*1000-time_repeat*1000)
time_repeat_np = time.time()
repeat_np()
print(time.time()*1000-time_repeat_np*1000)
    
