import numpy


class Point:
    def __init__(self, name: str, xCoordinate: float, yCoordinate: float):
        self.name = name
        self.xcoordinate = xCoordinate
        self.ycoordinate = yCoordinate

    def distance(self, anotherPoint, metric: int):
        if metric == 1:
            return abs(self.xcoordinate - anotherPoint.xcoordinate) + abs(
                self.ycoordinate - anotherPoint.ycoordinate
            )
        if metric == 2:
            return numpy.sqrt(
                (self.xcoordinate - anotherPoint.xcoordinate) ** 2
                + (self.ycoordinate - anotherPoint.ycoordinate) ** 2
            )

    def __repr__(self):
        repr = f"{self.name}({self.xcoordinate},{self.ycoordinate})"
        return repr

    @classmethod
    def originSymmetric(cls, point):
        return cls(
            point.name + "-origin symmetric", -point.xcoordinate, -point.ycoordinate
        )


# A = Point("A", 3, 4)
# B = Point("B", 7, 9)
# print(Point.distance(A, B, 1))
# print(Point.distance(A, B, 2))
# C = Point.originSymmetric(A)
# print(C.name, C.xcoordinate, C.ycoordinate)
# print(Point.__repr__(A))
