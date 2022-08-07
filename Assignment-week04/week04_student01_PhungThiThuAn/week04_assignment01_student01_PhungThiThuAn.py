A = [[1,2], [3,0,4], [2], [4,5]]
print('A =', A)

B = A.copy()
B.sort(key=lambda x: sum(x))
print('B =', B)

# thêm tiêu chí sắp xếp theo số lượng phần tử trong 2 list ổn bất kỳ.
C = A.copy()
C.sort(key=lambda x: len(x))
print('C =', C)

# A = [[1, 2], [3, 0, 4], [2], [4, 5]]
# B = [[2], [1, 2], [3, 0, 4], [4, 5]]
# C = [[2], [1, 2], [4, 5], [3, 0, 4]]
