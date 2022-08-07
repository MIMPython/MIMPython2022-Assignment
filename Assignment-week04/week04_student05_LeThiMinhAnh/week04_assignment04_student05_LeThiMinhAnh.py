from week04_assignment02_student05_LeThiMinhAnh import Point
from week04_assignment03_student05_LeThiMinhAnh import Line


def triangle_area(pointA, pointB, pointC):
    if pointA.distance(pointB, "L2") + pointB.distance(pointC, "L2") <= pointA.distance(pointC, "L2") or pointA.distance(pointB, "L2") + pointA.distance(pointC, "L2") <= pointB.distance(pointC, "L2") or pointB.distance(pointC, "L2") + pointA.distance(pointC, "L2") <= pointA.distance(pointB, "L2"):
        return 0
    else:
        BC = Line.lineFromPoints(pointB, pointC)
        h = BC.point_line_distance(pointA)
        return (1/2)*pointB.distance(pointC, "L2")*h


if __name__ == '__main__':
    pointA = Point(1, -2)
    pointB = Point(4, 0)
    pointC = Point(0, 0)
    print("Dien tich tam giac ABC:", triangle_area(pointA, pointB, pointC))
