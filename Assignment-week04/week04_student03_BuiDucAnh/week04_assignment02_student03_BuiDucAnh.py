from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, Point, metric):
        if metric == 'L1':
            dist = abs(self.x - Point.x) + abs(self.y - Point.y)
        if metric == 'L2':  
            dist = sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return dist

    def symmetry_point(self):
        return Point(-self.x, -self.y)

if __name__ == '__main__':
    pointA = Point(4, 2)
    pointB = Point(7, 6)
    print(pointA.distance(pointB, 'L2'))
    print(pointA.symmetry_point())
