import numpy
from matplotlib import pyplot as plt
from matplotlib import patches


class Point:
    def __init__(self, xCoordinate: float, yCoordinate: float):
        self.xcoordinate = xCoordinate
        self.ycoordinate = yCoordinate

    def distance(self, anotherPoint, metric=2):
        if metric == 1:
            return abs(self.xcoordinate - anotherPoint.xcoordinate) + abs(
                self.ycoordinate - anotherPoint.ycoordinate
            )
        else:
            return numpy.sqrt(
                (self.xcoordinate - anotherPoint.xcoordinate) ** 2
                + (self.ycoordinate - anotherPoint.ycoordinate) ** 2
            )

    def __repr__(self):
        repr = f"Point({self.xcoordinate},{self.ycoordinate})"
        return repr

    def plotting(self, pointColor: str, pointLabel: str):
        plt.plot(
            self.xcoordinate,
            self.ycoordinate,
            "o",
            color=pointColor,
            label=f"{pointLabel}",
        )

    @classmethod
    def originSymmetric(cls, point):
        return cls(-point.xcoordinate, -point.ycoordinate)


class Line:
    def __init__(self, a, b, c):
        """
        General equation of lines is ax + by + c = 0
        """
        self.a = a
        self.b = b
        self.c = c

    def conditions(self):
        if (
            (type(self.a) == float or type(self.a) == int)
            and (type(self.b) == float or type(self.b) == int)
            and (type(self.c) == float or type(self.c) == int)
        ):
            if self.a == 0 and self.b == 0:
                return 0
            return 1
        else:
            return 0

    def __repr__(self):
        if Line.conditions(self):
            repr = f"Line:\t{self.a}x + {self.b}y + {self.c} = 0"
        else:
            repr = f"Inputs are not a line."
        return repr

    def plotting(self, lineColor: str, lineLabel: str, x=numpy.linspace(-50, 50, 1001)):
        if self.b == 0:
            y = numpy.linspace(-20, 20, 1001)
            x = numpy.repeat(-self.c / self.a, 1001)
            plt.plot(x, y, "-", color=lineColor, label=lineLabel)
        else:
            y = -self.a * x / self.b - self.c / self.b
            plt.plot(x, y, "-", color=lineColor, label=lineLabel)

    @classmethod
    def intersection(cls, line, anotherLine):
        if line.a / line.b - anotherLine.a / anotherLine.b == 0:
            if line.c / line.a != anotherLine.c / anotherLine.a:
                return ()
            else:
                return "Two lines are the same."
        else:
            xCoordinate = (anotherLine.c * line.b - line.c * anotherLine.b) / (
                line.a * anotherLine.b - anotherLine.a * line.b
            )
            yCoordinate = (anotherLine.c * line.a - line.c * anotherLine.a) / (
                line.b * anotherLine.a - anotherLine.b * line.a
            )
            return Point(xCoordinate, yCoordinate)

    @classmethod
    def distanceFromAPoint(cls, line, point: Point):

        anotherLine = Line(
            -line.b,
            line.a,
            line.b * point.xcoordinate - line.a * point.ycoordinate,
        )
        projection = Line.intersection(line, anotherLine)
        return Point.distance(point, projection)

    @classmethod
    def linePassThroughTwoPoints(cls, point: Point, anotherPoint: Point):
        return cls(
            anotherPoint.ycoordinate - point.ycoordinate,
            point.xcoordinate - anotherPoint.xcoordinate,
            anotherPoint.xcoordinate * point.ycoordinate
            - anotherPoint.ycoordinate * point.xcoordinate,
        )


class Circle:
    def __init__(self, origin: Point, radius):
        self.origin = origin
        self.radius = radius

    def __repr__(self):
        repr = f"Circle with origin at ({self.origin.xcoordinate},\
            {self.origin.ycoordinate}) and radius {self.radius}."
        return repr

    def equation(self):
        return f"Circle equation:\
            (x - {self.origin.xcoordinate})^2 + (y - {self.origin.ycoordinate})^2 = {self.radius**2}"

    def plotting(self, circleColor, circleLabel, x=numpy.linspace(-50, 50, 1001)):
        y1 = self.origin.ycoordinate + numpy.sqrt(
            self.radius**2 - (x - self.origin.ycoordinate) ** 2
        )
        y2 = self.origin.ycoordinate - numpy.sqrt(
            self.radius**2 - (x - self.origin.ycoordinate) ** 2
        )
        plt.plot(x, y1, "-", color=circleColor, label=circleLabel)
        plt.plot(x, y2, "-", color=circleColor)

    @classmethod
    def circleFrom3Points(cls, A: Point, B: Point, C: Point):
        AB = Line.linePassThroughTwoPoints(A, B)
        BC = Line.linePassThroughTwoPoints(B, C)
        M = Point(
            0.5 * (A.xcoordinate + B.xcoordinate),
            0.5 * (A.ycoordinate + B.ycoordinate),
        )
        N = Point(
            0.5 * (B.xcoordinate + C.xcoordinate),
            0.5 * (B.ycoordinate + C.ycoordinate),
        )
        ABMidPerpendicular = Line(
            -AB.b,
            AB.a,
            AB.b * M.xcoordinate - AB.a * M.ycoordinate,
        )
        BCMidPerpendicular = Line(
            -BC.b,
            BC.a,
            BC.b * N.xcoordinate - BC.a * N.ycoordinate,
        )
        if (
            Point.distance(A, B, 2) + Point.distance(A, C, 2) <= Point.distance(B, C, 2)
            or Point.distance(A, B, 2) + Point.distance(B, C, 2)
            <= Point.distance(A, C, 2)
            or Point.distance(A, C, 2) + Point.distance(B, C, 2)
            <= Point.distance(A, B, 2)
        ):
            return f"These 3 points can't lie on the same circle."
        else:
            return cls(
                Line.intersection(ABMidPerpendicular, BCMidPerpendicular),
                Point.distance(
                    Line.intersection(ABMidPerpendicular, BCMidPerpendicular), A, 2
                ),
            )


if __name__ == "__main__":
    x = numpy.linspace(-100, 100, 101)
    y = numpy.linspace(-100, 100, 101)
    plt.figure(figsize=(10, 10))

    figure = plt.subplot()

    A = Point(3, 4)
    A.plotting("black", "A")

    B = Point(7, 10)
    B.plotting("yellow", "B")

    line1 = Line.linePassThroughTwoPoints(A, B)
    line1.plotting("red", "Line 1")

    line2 = Line(0, 1, 5)
    line2.plotting("blue", "AB")

    circle1 = Circle(A, 20)
    circle1.plotting("green", "Circle 1")

    C = Point(11, 20)
    C.plotting("cyan", "C")
    circle2 = Circle.circleFrom3Points(A, B, C)
    circle2.plotting("pink", "Circle 2")

    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)
    plt.legend(fontsize=14)
    plt.grid()
    figure.set_aspect(1)
    plt.savefig(
        ".\\additionalFolder\\week06_assignment03_student28_MaiThanhLiem_demo.png"
    )
    plt.show()
