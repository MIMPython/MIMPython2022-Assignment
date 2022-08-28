
import numpy as np
import time


# Min in numpy
def minUseNumpy(metrix):
        min = 100000000000
        size = len(metrix)
        for i in range(size):
            min = min(min,metrix[i])
        return min
    

# Max in numpy
def maxUseNumpy(metrix):
        max = -1
        size = len(metrix)
        for i in range(size):
            max = max(max,metrix[i])
        return max
 

    
if __name__ == '__main__':
    matrixNumpy = np.random.randint(100,size=(1000000))
    start = time.time()
    
    maxMatrixNumpy= maxUseNumpy(matrixNumpy)
    print(maxMatrixNumpy)
    print((time.time()- start) * 1000)
    secondstart = time.time()
    maxWithNumpy = matrixNumpy.max()
    print((time.time()- secondstart) * 1000)
    start = time.time()

    # Max in numpy: arr.max() or np.max(arr)
    # Time to perform: 1 ms 
    # Compare to arr.max(), whick takes about 271.57 ms.
    
    minMatrixNumpy = minNumpy(matrixNumpy)
    print(minMatrixNumpy)
    print((time.time()-start)*1000)
    Secondstart = time.time()
    minWithNumpy = matrixNumpy.min()
    print((time.time()- Secondstart)*1000)
    
  
# array.sum() or np.sum(arr): Sum of all elements of array.
# array.mean() or np.mean(arr): Average of all elements of array.
# np.median(array): Give the median of array
# np.zeros((4,6), dtype = int): Creat metrix (size: 4x6) 
