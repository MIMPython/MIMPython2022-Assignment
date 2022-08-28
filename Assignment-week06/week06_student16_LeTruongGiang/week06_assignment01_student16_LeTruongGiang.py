import numpy as np
import random
import time

#a
m,n = 500,500
def random_a(m,n):
    arr=[]
    for i in range(m):
        temp=[]
        for j in range(n):
            x = random.randint(0,9)
            temp.append(x)
        arr.append(temp)
    print(arr)
random_a(m,n)
print()

#b
array_b = np.random.randint(10, size=(m,n))

def sum_of_cols(array):
    arr=[]
    for i in range(0, len(array[0])):
        sum=0
        for j in range(0, len(array)):
            sum += array[j][i]
        arr.append(sum)
    print(arr)
sum_of_cols(array_b)
print()

#c
def randArr(m, n):
    arr1 = np.random.randint(10, size=(m,n))
    print(arr1)
randArr(m, n)
print()

def sum_of_cols_2(array):
    print(array.sum(axis=0))
sum_of_cols_2(array_b)
print()

#d
st_a = time.time()
random_a(m,n)
et_a = time.time()
elapsed_time_a = et_a - st_a

st_b = time.time()
sum_of_cols(array_b)
et_b = time.time()
elapsed_time_b = et_b - st_b

st_c1 = time.time()
randArr(m, n)
et_c1 = time.time()
elapsed_time_c1 = et_c1 - st_c1

st_c2 = time.time()
sum_of_cols_2(array_b)
et_c2 = time.time()
elapsed_time_c2 = et_c2 - st_c2

print("random array thông thường:")
print(elapsed_time_a)
print("random array numpy")
print(elapsed_time_c1)
print("tổng cột thông thường")
print(elapsed_time_b)
print("tổng cột numpy")
print(elapsed_time_c2)

