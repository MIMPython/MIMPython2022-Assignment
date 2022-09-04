print("Bài 1: List average")

import numpy as np

def listAverage(lst):
    try:
        if len(lst) != 0:
            k = np.mean(lst)
            return k
        else:
            return "ERRORR - Đây là mảng rỗng"
    except:
        return "ERROR - Những lỗi khác"

lst = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    try: 
        lst.append(int(input())) 
    except:
        pass
print(f"lst = {lst}")
print(listAverage(lst))
