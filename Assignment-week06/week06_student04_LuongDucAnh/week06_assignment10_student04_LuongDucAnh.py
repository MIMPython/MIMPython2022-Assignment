import numpy as np
from time import perf_counter

def det(matrix):
    #Kiểm tra xem ma trận có vuông không
    #Nếu không thì không có định thức
    if matrix.shape[0] != matrix.shape[1]:
        return None
    n = matrix.shape[0]
    result = 1
    for i in range(n): 
        #Kiểm tra phần tử trên đường chéo có bằng 0 không
        #Nếu có thì đổi chỗ với hàng có phần tử tại cột đó khác 0
        if matrix[i, i] == 0: 
            for j in range(i + 1, n):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]] #Đổi chỗ 2 hàng
                    #Khi đổi chỗ hai hàng, định thức đổi dấu do đó nhân (-1) để về giá trị ban đầu
                    result *= -1 
                    break
        if matrix[i, i] != 1:
            #Ở đây ta chia 1 hàng cho 1 số nên định thức cũng bị chia cho số đó
            #Do vậy ta cần nhân với số đó để định thức về giá trị ban đầu 
            result *= matrix[i, i]
            matrix[i] = matrix[i]/matrix[i, i]
        for j in range (i+1, n):
            if matrix[j, i] != 0:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]
    return result

a = np.random.randint(100, size=(101, 100)).astype(np.float64)
b = np.copy(a)

start1 = perf_counter()
mycode = det(a)
end1 = perf_counter()
deltat1 = end1 - start1

start2 = perf_counter()
numpydet = np.linalg.det(b)
end2 = perf_counter()
deltat2 = end2 - start2

print(f"My code: {mycode}\nExecution time: {deltat1}\n")
print(f"numpy.linalg.det: {mycode}\nExecution time: {deltat2}")