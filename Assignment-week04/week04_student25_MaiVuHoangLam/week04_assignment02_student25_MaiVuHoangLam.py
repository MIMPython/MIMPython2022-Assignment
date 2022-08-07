import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def return_x(self):
        return self.x

    def return_y(self):
        return self.y

    def __repr__(self):
        return repr('Coordinate: [' + str(self.x) + ', ' + str(self.y) + ']')

    def distance(self, pointB, metric):
        if metric == "L2":
            return math.sqrt(math.pow(self.x - pointB[0], 2) + math.pow(self.y - pointB[1], 2))
        elif metric == "L1":
            return math.fabs(self.x - pointB[0]) + math.fabs(self.y - pointB[1])

    def symetry_solution_2(self):
        C = [0, 0]
        C[0] = - self.x
        C[1] = - self.y
        return C


def simetry_solution_1(point):
    C = [0, 0]
    C[0] = - point.return_x()
    C[1] = - point.return_y()
    return C


if __name__ == '__main__':
    pointA = Point(4, 2)
    pointB = [4, 1]
    print(pointA.distance(pointB, metric="L2"))  # 1.0

    print(simetry_solution_1(pointA))  # [-4, 2]

    print(pointA.symetry_solution_2())  # [-4, 2]

    print(pointA.__class__.symetry_solution_2(pointA))  # [-4, 2]

    print(repr(pointA))  # 'Coordinate: [4, 2]'






