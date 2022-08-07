import math
import sympy as sp
from week04_assignment02_student23_HuaQuangHuy import Point
# class Line
"""
a, Đường thẳng y = ax + b không phải dạng tổng quát của phương trình đường thẳng với a, b bất kỳ. Ví dụ phương trình đường thẳng 5x + 3y - 1 = 0
b, điêù kiện của a, b, c để phương trình đường thẳng tồn tại là a != 0, b != 0
c, nhận xét đoạn code:
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

Nhận xét: đoạn code có hàm khởi tạo __init cho clas Line, nhưng hàm khởi tạo không xử lý trường hợp khi a = 0 và b = 0, nếu a và b cùng bằng 0 thì phương trình đường thẳng đó không tồn tại
"""


class Line:
    def __init__(self, a, b, c):
        if a == 0 and b == 0:
            print("he so cua a, b, c khong thoa man")
            return
        self.a = a
        self.b = b
        self.c = c
        print(f"Line {a}x + {b}y + {c} = 0 is created")

    def getIntersection(self, otherLine):
        aRatio = self.a / otherLine.a
        bRatio = self.b / otherLine.b
        cRatio = self.c / otherLine.c
        if aRatio != bRatio:
            x, y = sp.symbols('x y')
            line1 = sp.Eq(self.a * x + self.b * y + self.c, 0)
            line2 = sp.Eq(otherLine.a * x + otherLine.b * y + otherLine.c, 0)
            result_dictionary = sp.solve((line1, line2), (x, y))
            point = Point(result_dictionary[x], result_dictionary[y])
            return (point)
        if aRatio == bRatio and aRatio != cRatio:
            return ()
        if aRatio == bRatio and aRatio == cRatio:
            x = 0
            y = -self.c / self.b
            point = Point(x, y)
            return (point)

    def getDistance(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    @classmethod
    def getLineBy2Point(cls, pointA, pointB):
        if pointA.x == pointB.x and pointA.y == pointB.y:
            print("2 diem trung nhau ko xac dinh duong thang")
            return
        a, b = sp.symbols('a b')
        equation1 = sp.Eq(pointA.x * a - pointA.y + b, 0)
        equation2 = sp.Eq(pointB.x * a - pointB.y + b, 0)
        result_dictionary = sp.solve((equation1, equation2), (a, b))
        return cls(result_dictionary[a], -1, result_dictionary[b])


if __name__ == '__main__':
    line1 = Line(5, 3, 1)
    line0 = Line(6, 3, 1)
    point = Point(5, 7)
    pointB = Point(1, 8)
    print(line0.getIntersection(line1)) # Point (x-value=0, y-value=-1/3)
    print(line0.getDistance(point))  # 7.751702321999271
    # Line -1/4x + -1y + 33/4 = 0 is created
    line3 = Line.getLineBy2Point(point, pointB)
