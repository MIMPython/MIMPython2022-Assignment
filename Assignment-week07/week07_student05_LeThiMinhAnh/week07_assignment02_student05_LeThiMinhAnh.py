# 1) Xây dựng class Rectangle và class Square (kế thừa từ Rectangle). Thiết kế các thuộc tính, phương thức có liên quan
from math import *


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


rec1 = Rectangle(2, 3)
print(rec1.getArea())  # 6
square1 = Square(4)
print(square1.getArea())  # 16

# 1’) Bổ sung thêm class Rhombus và thực hiện kế thừa một cách phù hợp.


class Rhombus():
    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    def getArea(self):
        return self.side**2 * sin(radians(self.angle))


class Square(Rhombus):
    def __init__(self, side):
        super().__init__(side, 90)


print(Rhombus(4, 60).getArea())  # 13.856406460551018
square2 = Square(5)
print(square2.getArea())  # 25.0
# 2) Thực hiện yêu cầu tương tự với class Ellipse và class Circle.


class Ellipse():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return pi*self.a*self.b

    def getPerimeter(self):
        return pi*(3*(self.a+self.b)-sqrt((3*self.a+self.b)*(self.a+3*self.b)))


class Circle(Ellipse):
    def __init__(self, r):
        super().__init__(r, r)


print(Ellipse(5, 4).getPerimeter())  # 28.36166778425462
print(Circle(4).getPerimeter())  # 25.132741228718345
