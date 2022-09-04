import math

class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width
        self.diagonal = math.sqrt(length**2 + width**2)
    
    def getPerimeter(self):
        return 2*(self.length + self.width)
    
    def getArea(self):
        return self.length * self.width
    
    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def __repr__(self):
        return f"Square({self.length})"

class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.side = math.sqrt((diagonal1/2)**2 + (diagonal2/2)**2)
        
    def getArea(self):
        return (self.diagonal1 * self.diagonal2)/2
    
    def getPerimeter(self):
        return 4 * self.side
    
    def __repr__(self):
        return f"Rhombus({self.diagonal1}, {self.diagonal2})"
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getPerimeter(self):
        return 2*math.pi*self.radius
    
    def getArea(self):
        return math.pi*self.radius**2
    
    def __repr__(self):
        return f"Circle({self.radius})"
        
class Ellipse():
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    
    def __repr__(self):
        return f"Ellipse({self.major}, {self.minor})"
    
    def getPerimeter(self):
        return (2*math.pi*math.sqrt(((self.major**2) + (self.minor**2))/2))
    
    def getArea(self):
        return math.pi * self.major * self.minor
    
A = Rectangle(12,3)
print(A)
print(A.getArea())
print(A.getPerimeter())


B = Square(13)
print(B)
print(B.getArea())
print(B.getPerimeter())


C = Rhombus(2, 4)
print(C)
print(C.getArea())
print(C.getPerimeter())


D = Circle(5)
print(D)
print(D.getArea())
print(D.getPerimeter())

E = Ellipse(5, 10)
print(E)
print(E.getArea())
print(E.getPerimeter())