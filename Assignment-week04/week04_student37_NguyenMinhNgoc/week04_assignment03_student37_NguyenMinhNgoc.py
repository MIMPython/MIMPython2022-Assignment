"""
a) y = ax + b không phải là tổng quát của phương trình đường thẳng vì hệ số của y luôn là 1 khác 0 nên không 
thể biểu diễn được đường thẳng vuông góc với trục Ox (có dạng x = x0  với x0 là số thực bất kì) """

""" b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ. Tìm điều kiện của ba tham số a,b,c 
để phương trình này là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy."""
from week04_assignment02_student37_NguyenMinhNgoc import Point
import math as m
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        return
    def __str__(self):
        return str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + ' = 0' 
    def intersection_point(self, other):
        if self.a * other.b != self.b * other.a:
            x = (self.b * other.c - other.b * self.c) / (other.b * self.a - self.b * other.a)
            y = (self.a * other.c - other.a * self.c) / (other.a * self.b - self.a * other.b)
            return (x, y)
        else:
            if self.b * other.c != self.c * other.b:
                return ()
            else:
                return (1, -(self.a + self.c) / self.b)
    def distance_from_a_point(self, point):
        return abs(point.x * self.a + point.y * self.b + self.c) / m.sqrt(self.a * 2 + self.b * 2)
    def line_cross_2_points(pointA, pointB):
        vecABx = pointB.x - pointA.x
        vecABy = pointB.y - pointA.y
        vecx = 1.0
        vecy = - vecABx / vecABy
        return Line(vecx, vecy, -(vecx * pointA.x + vecy * pointA.y))
if __name__ == '_main_':
    LineA = Line(4, 2, 3)
    LineB = Line(7, 6, 4)
    point1 = Point(2, 3)
    point2 = Point(4, 5)
    print(LineA)
    print(LineA.intersection_point(LineB))
    print(LineA.distance_from_a_point(point1))
    print(Line.line_cross_2_points(point1, point2))