from array import array
from random import randint
import numpy as np
import time

#Hàm không sử dụng thư viện
def matrix1(m,n):
    array=[]
    for i in range(0,m):
        b=[]
        for j in range(0,n):
            b = b + [randint(1,100)]
        array=array+[b]
    return array

def sumCol1(array):
    result=[]
    for i in range(0,len(array[0])):
        sumCol=0
        for j in range(0,len(array)):
            sumCol += array[j][i]
        result += [sumCol]
    return result

#Hàm sử dụng thư viện
def matrix2(m,n):
    a=np.random.randint(100,size=(m,n))
    return a
def sumCol2(a):
    return a.sum(axis=0)

if __name__=='__main__':
    a=matrix1(3,2)
    print(a)
    print(sumCol1(a))
    print(time.time())

    b=matrix2(3,2)
    print(b)
    print(sumCol2(b))
    print(time.time())
   
    