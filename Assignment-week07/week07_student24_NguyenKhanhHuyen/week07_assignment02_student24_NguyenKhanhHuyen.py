import math


class Rectangle:
    @classmethod
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def areaRec(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def areaRhom(self):
        return (self.diagonal1*self.diagonal2)/2


class Square(Rectangle, Rhombus):
    def __init__(self, side):
        super().__init__(side, side)
        self.diagonal1 = math.sqrt(2*side*side)
        self.diagonal2 = math.sqrt(2*side*side)
    
square1 = Square(25)
print(square1.areaRec()) #625
print(square1.areaRhom())