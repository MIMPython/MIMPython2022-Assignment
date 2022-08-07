import math


class Point:
    x = 0.0
    y = 0.0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point, metric):
        if metric == 'L1':
            d = (self.x - point.x) ** 2 + (self.y - point.y) ** 2
            d = math.sqrt(d)
            return d
        else:
            d = abs(self.x - point.x) + abs(self.y - point.y)
            return d
    def getSymmetric(self):
        point = Point(- self.x, - self.y)
        return point
if __name__ == '__main__':
    A = Point(4, 2)
    

        