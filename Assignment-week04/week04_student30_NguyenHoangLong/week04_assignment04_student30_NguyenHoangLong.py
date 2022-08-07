"""Sử dụng công thức tính diện tích tam giác khi đã biết các tọa độ"""


def area_of_triangle(a, b, c):
    a1 = a[0]*(b[1] - c[1])
    a2 = b[0]*(c[1] - a[1])
    a3 = c[0]*(a[1] - b[1])
    return(0.5*(abs(a1 + a2 + a3)))

#A = (2, 5)
#B = (0, 3)
#C = (4, 0)
#print(area_of_triangle(A, B ,C)) # 7.0
