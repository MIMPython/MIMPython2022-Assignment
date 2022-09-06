import math
import scipy.integrate as integrate

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

class Square(Rectangle):
    
    def __init__(self, length):
        super().__init__(length,length)

class Rhombus():
    
    def __init__(self,diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self):
        edge = math.sqrt((self.diagonal1/2) ** 2 + (self.diagonal2/2) ** 2)
        return edge * 4
        
class Elipse():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        e = math.sqrt(self.a ** 2 - self.b **2) / self.a
        f = lambda x:math.sqrt(16*self.a**2-16*self.a**2*e**2*(math.sin(x))**2)
        result = integrate.quad(f,0,(math.pi)/2)
        for i in result:
            if i > 0:
                return i

class Circle(Elipse):
    
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.r = radius

    def perimeter(self):
        return 2 * math.pi * self.r


    