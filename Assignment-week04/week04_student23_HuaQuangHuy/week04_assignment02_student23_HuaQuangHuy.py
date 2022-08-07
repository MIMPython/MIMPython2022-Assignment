# Bai tap 2
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


# 2.4 tim diem doi xung qua goc toa do theo cach 1


def getSymmetricPoint(point):
    return Point(-point.x, -point.y)


if __name__ == '__main__':

    # 2.1: tạo lớp Point và tạo một số instance
    pointA = Point(2, 5)
    pointB = Point(7, 1)
    print(pointA.distance(pointA)) # 0.0
    print(pointA.distance2(pointB, metric='L1')) # 9

    symmetricPointA = getSymmetricPoint(pointA)  # (-2, -5)
    print(
        f"symmetric point of pointA through O is ({symmetricPointA.x},{symmetricPointA.y})")
    print(pointB.__repr__())
