import numpy as np
# Ý nghĩa một số hàm trong python
#1. mean: Tính giá trị trung bình các phần tử của mảng
#Vd:
arr=np.array([2,9,10,5], dtype=int)
print(np.mean(arr)) #6.5
#2. median: Tính giá trị trung vị của các phần tử trong mảng
#VD
print(np.median(arr)) #7.0
#3. max, min: Tìm giá trị lớn nhất, nhỏ nhất trong mảng
#Vd
print(np.max(arr)) #10
print(np.min(arr)) #2

# Thực hiện ý nghĩa các hàm trên không sử dụng thư viện numpy
# 1. mean
mean = sum(arr)/len(arr)
print(mean)
# 2. median
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
if len(arr) %2 ==1:
    median=arr[(int (len(arr)-2)/2)]
else:
    median=((arr[int (len(arr)/2-1)]+arr[int(len(arr)/2)]))/2
print(median)
# 3. max,min
max=arr[1]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
