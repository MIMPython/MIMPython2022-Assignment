from week04_assignment02_student31_TranVanLuat import Point
from math import sqrt
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        return None
     
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c
    
    def isLine(self):
        return (self.getA()**2 + self.getB()**2) > 0
    
    
    def distance(point,self):
        return abs(point.getX()*self.getA()+point.getY()*self.getB()+self.getC)/sqrt(self.getA()**2 + self.getB()**2)
    
    def intersection(self, line):
        if self.getA() * line.getB() == self.getB()* line.getA():
            if self.getB() * line.getC() != self.getC() * line.getB():
                return ()
            else:
                return (1, -(self.getA() + self.getC()) / self.getB())
        else:
            x = (self.getB() * line.getC() - line.getB() * self.getC()) / (line.getB() * self.getA() - self.getB() * line.getA())
            y = (self.getA() * line.getC() - line.getA() * self.getC()) / (line.getA() * self.getB() - self.getA() * line.getB())
            return (x, y)
            
            
    def line(point1, point2):
        ABx = point2.x - point1.x
        ABy = point2.y - point1.y
        x = 1.0
        y = - ABx / ABy
        newLine = Line(x, y, -(x * point1.getX() + y * point1.getY()))
        return newLine
    
if __name__ == '__main__':
    LineA = Line(4,5,6)
    LineB = Line(3,4,5)
    point1 = Point(0,1)
    point2 = Point(2,3)
    print(LineA)
    print(LineA.intersection(LineB))
    print(LineA.distance(point1))
    print(Line.line(point1, point2))
    
    