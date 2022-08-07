def area(pointA, pointB, pointC):
   return abs((pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) - (pointC[0] - pointA[0]) * (pointB[1] - pointA[1]))/2

def point(x, y):
    sef = list()
    sef.append(x)
    sef.append(y)
    return sef

A = point(0, 1)
B = point(2, 0)
C = point(0, 0)
S = area(A, B, C)
if (S == 0):
    print( "3 điểm đã cho không tạo thành tam giác")
else:
    print("diện tích tam giác đã cho là: ", S, sep = "")