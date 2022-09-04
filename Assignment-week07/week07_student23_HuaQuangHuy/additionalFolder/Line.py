import sympy as sp
import math
from additionalFolder import Point


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
