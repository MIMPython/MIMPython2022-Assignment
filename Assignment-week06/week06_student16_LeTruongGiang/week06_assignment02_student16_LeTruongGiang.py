import numpy as np
import time

np.random.seed(10)

def randArr(m, n):
    arr1 = np.random.randint(20, size=(m,n))
    print(arr1)
    return arr1
array = randArr(10,12)

'''
np.mean(array): trả về giá trị trung bình cộng của tất cả các phần tử có trong một mảng.
'''
def mean():
    print('mean')
    #numpy
    print(np.mean(array)) 

    #normal
    m = len(array)
    n = len(array[0])
    sum_by_rows = 0
    for i in range(m):
        sum_by_rows += sum(array[i])
    print(sum_by_rows/(m*n))
mean()

'''
np.median(ndarray): trả về giá trị trung vị của một mảng đã cho 
'''
def median():
    print('median')
    print(np.median(array))
    
    B=[]
    for i in range(len(array)):
        for j in array[i]:
            B.append(j)
    B.sort()
    md = 0
    if len(B)%2 == 0:
        md = (B[int(len(B)/2 - 1)] + B[int(len(B)/2)])/2
    else:
        md = B[len(B)//2]
    print(md) 
median()

'''
np.max(array): trả về phần tử có giá trị lớn nhất trong mảng
'''
def max_():
    print('max')
    print(array.max())
    
    B=[]
    for i in range(len(array)):
        for j in array[i]:
            B.append(j)
    B.sort()
    print(B[-1])
max_()


'''
np.min(array): trả về phần tử có giá trị nhỏ nhất trong mảng
'''
def min_():
    print('min')
    print(array.min())
    
    B=[]
    for i in range(len(array)):
        for j in array[i]:
            B.append(j)
    B.sort()
    print(B[0])
min_()


'''
np.argmax(array): trả về vị trí của giá trị lớn nhất (đầu tiên)
'''
def argmax_():
    print('argmax')
    print(array.argmax())
    
    B=[]
    for i in range(len(array)):
        for j in array[i]:
            B.append(j)
            
    max = B[0]
    index=0
    for i in range(1,len(B)):
        if B[i] > max:
            max = B[i]
            index = i
    print(index)
        
argmax_()


'''
np.argmin(array): trả về vị trí của giá trị nhỏ nhất (đầu tiên)
'''
def argmin_():
    print('argmin')
    print(array.argmin())
    
    B=[]
    for i in range(len(array)):
        for j in array[i]:
            B.append(j)
            
    min = B[0]
    index=0
    for i in range(1,len(B)):
        if B[i] < min:
            min = B[i]
            index = i
    print(index)
argmin_()

