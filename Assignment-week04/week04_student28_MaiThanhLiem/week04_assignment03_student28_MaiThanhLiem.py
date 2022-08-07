from week04_assignment02_student28_MaiThanhLiem import Point


class Line:
    def __init__(self, name, a, b, c):
        self.name = name
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
        if Line.conditions(self) == 1:
            repr = f"Line {self.name}:\t{self.a}x + {self.b}y + {self.c} = 0"
        else:
            repr = f"Inputs are not a line."
        return repr

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
            return Point("Intersection", xCoordinate, yCoordinate)

    @classmethod
    def distanceFromAPoint(cls, line, point: Point):

        anotherLine = Line(
            "Perpendicular Line",
            -line.b,
            line.a,
            line.b * point.xcoordinate - line.a * point.ycoordinate,
        )
        projection = Line.intersection(line, anotherLine)
        return Point.distance(point, projection, 2)

    @classmethod
    def linePassThroughTwoPoints(cls, point: Point, anotherPoint: Point):
        return cls(
            "Line pass through two points",
            anotherPoint.ycoordinate - point.ycoordinate,
            point.xcoordinate - anotherPoint.xcoordinate,
            anotherPoint.xcoordinate * point.ycoordinate
            - anotherPoint.ycoordinate * point.xcoordinate,
        )


# (a)
"""
The Line equation y = ax + b with a, b to be the arbitrary parameter isn't
the gerenal equation for lines in xy plane, because it doesn't represent all lines possible.
"""
# lineA = Line("Horizontal Axis", 1, 0, 0)
# print(Line.__repr__(lineA))

# (b)
"""
Parameters a, b, c have to satysfied the following conditions:
- a, b, c are real numbers;
- a, b are not simultaneously equal to zero.
"""
# lineB = Line("B", 0, 0, 0)
# print(Line.__repr__(lineB))
# lineC = Line("C", "0", 1, 2)
# print(Line.__repr__(lineC))

# (c)
"""
```
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
```
The initializing a Line class in above snippet is ok, but we need more than that 
to make a general equation for lines in xy plane: conditions for parameter a, b, c.
"""
# (d)
# line1 = Line("1", 1, 2, 0)
# line2 = Line("2", 4, 5, 20)
# print(Line.intersection(line1, line2))

# (e)
# M = Point("M", 2, 1)
# print(Line.distanceFromAPoint(line1, M))

# (f)
# N = Point("N", 3, 9)
# print(Line.linePassThroughTwoPoints(M, N))
