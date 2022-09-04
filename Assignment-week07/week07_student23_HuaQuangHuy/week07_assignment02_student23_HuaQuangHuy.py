# excersise  2: class inheritance
import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2*(self.width + self.height)

# class Square inheritance from Rectangle


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

# class Rhombus inheritance from Square


class Rhombus(Square):
    def __init__(self, width, angel):  # width is width of edge,
        super().__init__(width)
        self.angel = angel

    def getArea(self):
        return self.width ** 2 * math.sin(math.radians(self.angel))

# class Elipse


class Elipse:
    def __init__(self, x, y, hradius, vradius, eccentricity):
        self.x = x
        self.y = y
        self.hradius = hradius
        self.vradius = vradius
        self.eccentricity = eccentricity

    def getArea(self):
        return self.hradius * self.vradius * math.pi

    def getPerimeter(self):
        radius = math.sqrt((self.hradius ** 2 + self.vradius ** 2) / 2)
        return 2 * math.pi * radius


class Circle(Elipse):
    def __init__(self, x, y, radius, eccentricity):
        super().__init__(x, y, radius, radius, eccentricity)


if __name__ == '__main__':
    rectangle = Rectangle(2, 3)
    square = Square(2)
    rhombus = Rhombus(2, 120)

    print(rhombus.getArea())  # 3.46
    print(rhombus.getPerimeter())  # 8

    print(square.getArea())  # 4
    print(square.getPerimeter())  # 8

    print(rectangle.getArea())  # 6
    print(rectangle.getPerimeter())  # 10
