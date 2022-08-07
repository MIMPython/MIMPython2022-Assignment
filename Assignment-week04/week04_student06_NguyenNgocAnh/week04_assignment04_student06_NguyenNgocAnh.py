import math
import sympy as sp
from week04_assignment02_student06_NguyenNgocAnh import Point
from week04_assignment03_student06_NguyenNgocAnh import Line


def area1(point1, point2, point3):
    l1 = Line.find_line(point1, point2)
    distance_1_2 = point1.distance(point2, 'L2')
    print(distance_1_2)
    height = l1.distance_point_to_line(point3)
    area = 1 / 2 * distance_1_2 * height
    return area


def area2(point1, point2, point3):
    dist1 = point1.distance(point2, 'L2')
    dist2 = point2.distance(point3, 'L2')
    dist3 = point3.distance(point1, 'L2')

    area = sp.sqrt((dist1 + dist2 + dist3) * (- dist1 + dist2 + dist3)* (dist1 - dist2 + dist3) * (dist1 + dist2 - dist3)) / 4
    return area


if __name__ == '__main__':
    A = Point(1, 0)
    B = Point(0, 1)
    C = Point(0, 0)

    print(area1(A, B, C))
    print(area2(A, B, C))
