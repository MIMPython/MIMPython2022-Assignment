import numpy as np

def np_mean(a):
    return sum(a)/len(a)

def np_median(a):
    a = np.sort(a)
    if len(a) % 2 == 0:
        mid = len(a) // 2
        return (a[mid] + a[mid - 1]) / 2
    else:
        return a[int(len(a)/2)]

def np_max(a):
    maxx = -np.inf
    for x in a:
        maxx = max(x, maxx)
    return maxx

def np_min(a):
    minn = np.inf
    for x in a:
        minn = min(x, minn)
    return minn
def np_argmax(a):
    maxx = -np.inf
    pos = 0
    for i in range(a):
        if a[i] > maxx:
            maxx = a[i]
            pos = i
    return pos

def np_argmin(a):
    minn = np.inf
    pos = 0
    for i in range(a):
        if a[i] < minn:
            minn = a[i]
            pos = i
    return pos

def np_arange(a, b, c):
    arr = []
    for i in range(a, b, c):
        arr.append(i)
    return arr

def np_repeat(a, n):
    res = []
    for i in range(len(a)):
        for j in range(n):
            res.append(a[i])
    return res

if __name__ == "__main__":
    a = np.array([11, 99, 0, 5, 14, 89, 23, 7, 1, 10])
    print(np.mean(a)) # 25.9 return to the average value of the array
    print(np_mean(a))  # 25.9
    print(np.median(a)) # 10.5 return to the median value of the array
    print(np_median(a)) # 10.5
    print(np.max(a))  # 99 return to the maximum element of the array
    print(np_max(a))  # 99
    print(np.min(a))  # 0 return to the minimize element of the array
    print(np_min(a))  # 0
    print(np.argmax(a)) # 1 return to the position of the max element
    print(np_argmax(a)) # 1
    print(np.argmin(a)) # 2 return to the position of the min element
    print(np_argmin(a)) # 2
    print(np.linspace(1, 5, num = 5, endpoint = True)) # [1. 2. 3. 4. 5.] create an arithmetic sequence
    print(np.arange(1, 5, 1)) # [1 2 3 4] similar to linspace
    print(np_arange(1, 5, 1)) # [1 2 3 4]
    print(np.repeat(a, 2))  # [11 11 99 99  0  0  5  5 14 14 89 89 23 23  7  7  1  1 10 10] Output array which has the same shape as a, except along the given axis.
    print(np_repeat(a, 2))  # [11 11 99 99  0  0  5  5 14 14 89 89 23 23  7  7  1  1 10 10]
    print(np.random.rand(1, 5)) # [[0.31670226 0.50806049 0.10601295 0.52510078 0.13722096]]  Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
    print(np.ones((2, 3)))  # [[1. 1. 1.] [1. 1. 1.]] return to an one matrix
    print(np.zeros((2, 2)))   # [[0. 0.] [0. 0.]] return to an zero matrix
    print(np.where(a<50, a*2, a)) # [22 99  0 10 28 89 46 14  2 20]
    np_where = [2*a[i] if a[i] < 50 else a[i] for i in range(len(a))]
    print(np_where) # [22, 99, 0, 10, 28, 89, 46, 14, 2, 20]



