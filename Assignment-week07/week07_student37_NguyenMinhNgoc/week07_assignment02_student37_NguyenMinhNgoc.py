import math as m
class LengthException(Exception):
    pass
class Rectangle:
    def __init__(self, width, height):
        try:
            self.width = width
            self.height = height
            if self.width <= 0 or self.height <= 0:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, size):
        try:
            self.width = size
            self.height = size
            if self.width <= 0 or self.height <= 0:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        try:
            self.diagonal1 = diagonal1
            self.diagonal2 = diagonal2
            if self.diagonal1 <= 0 or self.diagonal2 <= 0:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def perimeter(self):
        return 2 * m.sqrt(self.diagonal1 * 2 + self.diagonal2 * 2)
    def area(self):
        return self.diagonal1 * self.diagonal2 / 2
class Circle:
    def __init__(self, radius):
        try:
            self.radius = radius
            if self.radius <= 0 :
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def perimeter(self):
        return 2 * self.radius * m.pi
    def area(self):
        return self.radius * self.radius * m.pi
class Ellipse:
    def __init__(self, major_radius, minor_radius):
        try:
            self.major_radius = major_radius
            self.minor_radius = minor_radius
            if self.minor_radius <= 0 or self.major_radius <= 0:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def perimeter(self):
        h = (self.major_radius - self.minor_radius) * 2 / (self.major_radius + self.minor_radius) * 2
        return m.pi * (self.major_radius + self.minor_radius) * (1 + 3 * h / (10 + m.sqrt(4 - 3 * h))) #Ramanujan approximation formula
    def area(self):
        return self.major_radius * self.minor_radius * m.pi
if __name__ == '__main__':
    s = Square(-2)
    r = Rectangle(2, 3)
    rh = Rhombus(4, 3)
    print(rh.perimeter())
    print(r.area())
    c = Circle(9)
    print(c.perimeter())
    e = Ellipse(2, 3)
    print(e.area())
    print(e.perimeter())