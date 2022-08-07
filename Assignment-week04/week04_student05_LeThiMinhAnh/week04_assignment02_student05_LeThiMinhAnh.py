from math import sqrt


class Point:
    """Initialize class."""

    def __init__(self, x, y):
        """Initialize x coordinate and y coordinate points."""
        self.x = x
        self.y = y

    def distance(self, pointB, metric):
        if metric == "L2":
            return sqrt((self.x-pointB.x)**2 + (self.y-pointB.y)**2)
        else:
            return abs(self.x-pointB.x) + abs(self.y-pointB.y)

    def getSymmetry(self):
        return Point(-self.x, -self.y)

    def __repr__(self):
        return "Point (%s, %s)" % (self.x, self.y)


if __name__ == '__main__':
    pointA = Point(1, 2)
    pointB = Point(3, 0)
    print(pointA.distance(pointB, "L2"))  # 2.8284271247461903
    print(pointB.distance(pointA, "L1"))  # 4
    print(repr(pointA.getSymmetry()))  # Point (-1, -2)
