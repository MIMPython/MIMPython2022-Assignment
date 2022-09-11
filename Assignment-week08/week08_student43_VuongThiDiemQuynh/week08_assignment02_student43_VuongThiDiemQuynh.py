'''
Bài tập 2. (solving linear equations)
Viết một hàm thực hiện giải phương trình tuyến tính Ax=b với A,b lần lượt là ma trận, vector (với kích thước phù hợp) cho trước. So sánh (độ chính xác, thời gian thực thi của) hàm vừa viết với hàm dựng sẵn trong thư viện numpy
'''


def solvingLinearEquations(A, B):
    
    # Get number of row and col of matrix A
    rowsOfA = len(A)
    colsOfA = len(A[0])

    # Get number of row and col of matrix B
    rowsOfB = len(B)
    colsOfB = len(B[0])
    
    # Initialize matrix result C
    C = []

    # Loop to solve equations
    for i in range(rowsOfA):
        for j in range(colsOfB):
            total = 0
            for k in range(colsOfA):
                total += A[i][k] * B[k][j]
            C.append(total)
    return C


if __name__ == '__main__':

    A = [[5, 3, 1], [3, 9, 4], [1, 3, 5]]

    B = [[9], [16], [9]]

    test = solvingLinearEquations(A, B)

    print(test) # [102, 207, 102]