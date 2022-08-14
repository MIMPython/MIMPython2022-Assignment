import math
from week04_assignment02_student23_HuaQuangHuy import Point


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def getCircumference(self):
        return self.radius * 2 * math.pi

    def getArea(self):
        return self.radius ** 2 * math.pi


if __name__ == '__main__':
    center = Point(0, 0)
    circle1 = Circle(center, 5)
    print(
        f"Circle: center: ({circle1.center.x}, {circle1.center.y}), radius: {circle1.radius}")  # Circle: center: (0, 0), radius: 5
    print(circle1.getCircumference())  # 31.41592653589793
    print(circle1.getArea()) # 78.53981633974483
