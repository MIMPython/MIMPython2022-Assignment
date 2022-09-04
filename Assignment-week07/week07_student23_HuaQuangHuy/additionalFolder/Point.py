import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # phuong thuc distance tinh khoang cach euclid

    def distance(self, otherPoint):
        return math.sqrt((otherPoint.x - self.x) ** 2 + (otherPoint.y - self.y) ** 2)
    # phuong thuc distance tinh khoang cach co metric

    def distance2(self, otherPoint, metric):
        if metric == 'L2':
            self.distance(otherPoint)
        if metric == 'L1':
            return abs(self.x - otherPoint.x) + abs(self.y - otherPoint.y)
    # 2.5

    def __repr__(self):
        return f'Point (x-value={self.x}, y-value={self.y})'