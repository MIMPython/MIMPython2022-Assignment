import numpy as np
from matplotlib import pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    
    def distance(self, other, metric):
        if metric == "L1":
            return abs(self.x - other.x) + abs(self.y - other.y)
        elif metric == "L2":
            return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def getSymmetric(self):
        return Point(-self.x, -self.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def plot(self, color = "black"):
        plt.plot(self.x, self.y, "go", color = color)

    
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
        return abs(self.a * point.x + self.b * point.y + self.c)/np.sqrt(self.a**2 + self.b**2)
    
    @classmethod
    def lineFromPoints(cls, A:Point, B:Point):
        a = B.y - A.y
        b = A.x - B.x
        c = -a * A.x - b * A.y
        return cls(a, b, c)
    
    def plot(self, color = "blue"):
        if self.b != 0:
            f = lambda x: (-self.a/self.b) * x -self.c/self.b
            x = np.linspace(-10, 10, 1000)
            y = f(x)
            plt.plot(x, y, '-', color=color)
    
class Circle:
    def __init__(self, center:Point, radius):
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"
    
    def plot(self, color = "red"):
        f = lambda x: np.sqrt(self.radius**2 - (x - self.center.x)**2) + self.center.y
        g = lambda x: -np.sqrt(self.radius**2 - (x - self.center.x)**2) + self.center.y
        x = np.linspace(-10, 10, 1000000)
        plt.plot(x, f(x), "-", color = color)       
        plt.plot(x, g(x), "-", color = color) 
        

A = Point(3, 2)
A.plot()
B = Point (1, 0)
B.plot()
d = Line.lineFromPoints(A, B)
d.plot()
C = Circle(A, 5)
C.plot()
plt.show()