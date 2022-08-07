"""
a) y = ax + b không phải phương trình tổng quát của đường thẳng trong mặt phẳng Oxy vì nó không biểu diễn được các đường thẳng 
dạng x = x0 (X0 là số thực bất kì) vuông góc với trục Ox.

b) Để pt ax + by + c = 0 là pt tổng quát của 1 đường thẳng thì: a^2 + b^2 > 0
nghĩa là a, b không đồng thời bằng 0.
"""

from cmath import sqrt
from week04_assignment02_student03_BuiDucAnh import Point

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + ' = 0' 

    #intersection of two lines
    def intersection_of_two_lines(self, LineB):
        delta = self.a * LineB.b - LineB.a * self.b
        if delta != 0:
            x = (-self.c * LineB.b + LineB.c * self.b) / delta
            y = (self.a * (-LineB.c) + LineB.a * self.c) / delta
            return (x, y)
        else:
            if (self.b * (-LineB.c) + LineB.b * self.c) != 0:
                return ()
            else:
                return (1, (-self.c - self.a) / self.b)
    
    #distance from point to line
    def distance_from_point_to_line(self, Point):
        return abs(self.a * Point.x + self.b * Point.y + self.c) / sqrt(self.a**2 + self.b**2)
    
    #straight line passing through 2 points
    def line_pass_two_point(pointA, pointB):
        vecto1 = pointA.x - pointB.x
        vecto2 = pointA.y - pointB.y
        return Line(-vecto2, vecto1, vecto2*pointA.x - vecto1*pointA.y )

if __name__ == '__main__':
    lineA = Line(1, 2, 3)
    lineB = Line(4, 5, 6)
    pointA = Point(7, 8)
    pointB = Point(9, 10)
    print(lineA)
    print(lineB)
    print(lineA.intersection_of_two_lines(lineB))
    print(lineA.distance_from_point_to_line(pointA))
    print(Line.line_pass_two_point(pointA, pointB))