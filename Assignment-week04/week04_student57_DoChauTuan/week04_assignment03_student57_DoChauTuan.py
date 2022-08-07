# Bai 3

# a) khong the bieu dien vertical line (y = c) hoac horizontal line (x = c) qua phuong trinh y = ax + b
# b) a != 0 and b != 0 cung luc
# c) kho de hieu a, b, c co y nghia gi voi Line nen them comments

class Line:
    """ax + by + c = 0"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_intersect_points(self, line):
        try:
            if self.a == line.a and self.b == line.b and self.c == line.c:
                raise ValueError("infinite roots")
            elif self.a * line.b == self.b * line.a and self.c != line.c:
                raise ValueError("no roots")
            else:
                x = (self.b * line.c - self.c * line.b) / (self.a * line.b - self.b * line.a)
                y = (self.c * line.a - self.a * line.c) / (self.a * line.b - self.b * line.a)
                return (x, y)
        except ValueError as ve:
            return ve

    def get_distance_point(self, point):
        square = lambda x: x ** 2
        square_root = lambda x: x ** (1 / 2)
        dis = abs(self.a * point.x + self.b * point.y + self.c) / square_root(square(self.a) + square(self.b))
        return dis

    @classmethod
    def line_through__two_points(cls, point1, point2):
        slope = (point2.y - point1.y) / (point2.x - point1.x)
        return cls(slope, -1, point1.y - point1.x * slope)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    l1 = Line(3, -4, 5)
    l2 = Line(1, -2, 3)
    print(l1.get_intersect_points(l2))  # (1.0, 2.0)
    l3 = Line(1, 2, 5)
    l4 = Line(1, 2, -3)
    print(l3.get_intersect_points(l4))  # no roots
    l5 = Line(2, 2, 2)
    l6 = Line(2, 2, 2)
    print(l5.get_intersect_points(l6))  # infinite roots
    x1 = Point(3, 4)
    print(l1.get_distance_point(x1))  # 0.4
    x2 = Point(1, 2)
    l_new = Line.line_through__two_points(x1, x2)
    print(l_new.a)  # 1.0
    print(l_new.b)  # -1
    print(l_new.c)  # 1.0