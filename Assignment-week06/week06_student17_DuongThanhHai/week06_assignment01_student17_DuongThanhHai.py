
import random 
import numpy as np

# cau a,b
def inputArray ():
    #row
    m = int(input())
    #collumn
    n = int(input())

    array = []
    for i in range (m):
        r = []
        for j in range (n):
            r.append(random.randint(0,100))
        array.append(r)
    
    return array

def sumCollumn(array,r,c):
    for i in range (c):
        sum = 0
        for j in range(r):
            sum += array[j][i]
        print (sum, end = ' ')


array = inputArray()
r = len(array)
c = len(array[0])
for i in range (r):
    for j in range(c):
        print (array[i][j], end=' ')
    print()

sum_of_each_collumn = sumCollumn(array,r ,c)


# cau c
def sumCol_c():
    m = int(input())
    n = int(input())

    array = np.random.randint(0,100, (m,n))
    print (array)

    sum = np.sum(array, axis = 0)
    print(sum)

sumCol_c()

    


    
