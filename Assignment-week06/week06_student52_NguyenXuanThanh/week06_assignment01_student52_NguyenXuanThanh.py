import random
import numpy as np
#a
def foo (m,n):
    val = [1] * m
    for j in range (m):
        val[j] = [1] * n
        for i in range(n):
            val[j][i] = random.randint(0,9)
    return val
array = foo(3, 5)
print(array)
'''[[9, 1, 2, 8, 7], 
[9, 5, 2, 4, 5], 
[6, 7, 5, 9, 7]]'''
#b
def bar(array):
    a = [0]*len(array[0])
    for i in range(len(array[0])):
        for j in range(len(array)):
            a[i] += array[j][i]
    return a
print(bar(array))
# [24, 13, 9, 21, 19]
#c
arr = np.ndarray((3,5), int)
print(arr)
'''[[                  0                   0 4601727903846100441
  4587820456862672466 4595745948572889240]
 [4601727903846100441 4596827656117413458 4600249548200259736
  4601727903846100441 4602288710223143708]
 [4603108665757041778 4601727903846100441 4605834855372154450
  4604753147827630232 4601727903846100441]]'''
print(arr.sum(axis=0))
'''[ 9204836569603142219  9198555559963513899 -4638931766291036989
 -4652442565173148477 -4646981511067418227]'''