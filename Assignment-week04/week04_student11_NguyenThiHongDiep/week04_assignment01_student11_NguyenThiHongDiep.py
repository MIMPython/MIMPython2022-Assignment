# Sắp xếp list theo thứ tự tăng dần của tổng các số trong mỗi list con
def sortList1(A):
    A.sort(key = lambda x: sum(x))
    return A

# Sắp xếp list theo thứ tự giảm dần của giá trị max trong mỗi list con
def sortList2(A):
    A.sort(key = lambda x: max(x), reverse = True)
    return A

if __name__ == '__main__':
    A1 = [[0, -1], [2], [-7, 1], [-6, 7, 0], [1, -9, 8]]
    print('A =', A1)
    print('B =', sortList1(A1))
    print('C =', sortList2(A1))

# A = [[0, -1], [2], [-7, 1], [-6, 7, 0], [1, -9, 8]]
# B = [[-7, 1], [0, -1], [1, -9, 8], [-6, 7, 0], [2]]
# C = [[1, -9, 8], [-6, 7, 0], [2], [-7, 1], [0, -1]]

    A2 = [[15, -11], [80, -80], [-14, 8], [1, 2, -11], [23], [10, 10, -74], [6, 2, 0, 0, 1]]
    print('A =', A2)
    print('B =', sortList1(A2))
    print('C =', sortList2(A2))

# A = [[15, -11], [80, -80], [-14, 8], [1, 2, -11], [23], [10, 10, -74], [6, 2, 0, 0, 1]]
# B = [[10, 10, -74], [1, 2, -11], [-14, 8], [80, -80], [15, -11], [6, 2, 0, 0, 1], [23]]
# C = [[80, -80], [23], [15, -11], [10, 10, -74], [-14, 8], [6, 2, 0, 0, 1], [1, 2, -11]]