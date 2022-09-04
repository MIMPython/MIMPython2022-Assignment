import math
from .point import Point

class Line:
    def __new__(cls, a, b, c):
        if a**2 + b **2 != 0:
            obj = super().__new__(cls)
            obj.a, obj.b, obj.c = a, b, c
            return obj
        else:
            print ("Invalid line, a and b are not all simultaneously equal to zero")
            return None

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"
        
    def findLineIntersection(self, other):
        det = self.a * other.b - other.a * self.b
        if det == 0:
            if self.b != 0:
                if other.a + other.b * (-self.c - self.a)/self.b == -other.c:
                    return "infinite roots"
            elif self.a != 0:
                if other.b + other.a * (-self.c - self.b)/self.a == -other.c:
                    return "infinite roots"
            return ()
        else:
            x = (other.b * (-self.c) - self.b * (-other.c))/det
            y = (self.a * (-other.c) - other.a * (-self.c))/det
            return (Point(x, y),)
    
    def getDistance(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c)/math.sqrt(self.a**2 + self.b**2)
    
    @classmethod
    def lineFromPoints(cls, A, B):
        a = B.y - A.y
        b = A.x - B.x
        c = -a * A.x - b * A.y
        return cls(a, b, c)