from asyncio.windows_events import NULL
from turtle import distance
from week04_assignment02_student24_NguyenKhanhHuyen import Point
import math
class Line:
    def __init__(self, a, b, c):
        if a**2 + b**2 != 0:
            self.a = a
            self.b = b
            self.c = c
    def __repr__(self): 
       return f"{self.a}*x + {self.b}*y + {self.c}"
    def giaoDiem(self, lineB):
        if self.a/lineB.a == self.b/lineB.b and self.a/lineB.a != self.c/lineB.c:
            return tuple(NULL)
        elif self.a/lineB.a == self.b/lineB.b and self.a/lineB.a == self.c/lineB.c:
            return "Có vô số giao điểm"
        else:
            D = (self.a * lineB.b)-(lineB.a *self.b)
            Dx = (lineB.c * self.b)-(self.c* lineB.b)
            Dy = (lineB.a * self.c)-(self.a*lineB.c)
            x = Dx /D
            y= Dy/D
            return (x,y)

    def distance(self, point):
        tu_so = abs(self.a * point.x +self.b* point.y + self.c)
        mau_so = math.sqrt(self.a**2 + self.b**2)
        return tu_so/mau_so

    @classmethod
    def newLine(cls, pA, pB):
        a = pA.y - pB.y
        b = pB.x - pA.x
        c = (pA.y - pB.y)*(-pA.x) + (pB.x - pA.x)*(-pA.y)
        return cls(a, b, c)

if __name__ == '__main__':
    line1 = Line(7, 3, -4)
    line2 = Line(-9, 2, 10)
    pointA = Point(4, 2)
    pointB = Point(5, 6)
    lineC = Line.newLine(pointA, pointB)
    print(line1.giaoDiem(line2)) #(0.926..., -0.829...)
    print(line1.distance(pointA)) #3.93...
    print(lineC)
