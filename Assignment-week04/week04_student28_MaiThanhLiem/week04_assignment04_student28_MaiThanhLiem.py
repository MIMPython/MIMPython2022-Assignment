from week04_assignment02_student28_MaiThanhLiem import Point
from week04_assignment03_student28_MaiThanhLiem import Line


def area(A: Point, B: Point, C: Point):
    AB = Line.linePassThroughTwoPoints(A, B)
    BC = Line.linePassThroughTwoPoints(B, C)
    AC = Line.linePassThroughTwoPoints(A, C)
    return 0.5 * Line.distanceFromAPoint(AB, C) * Point.distance(A, B, 2)


A = Point("A", 1, 3)
B = Point("B", 12, 32)
C = Point("C", 7, 15)
print(area(A, B, C))
