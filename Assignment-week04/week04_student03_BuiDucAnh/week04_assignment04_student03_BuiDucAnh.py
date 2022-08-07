from cmath import sqrt
from week04_assignment02_student03_BuiDucAnh import Point
from week04_assignment03_student03_BuiDucAnh import Line

class Triangle:

    # User heron
    def triangle_area_heron(pointA, pointB, pointC):
        AB = pointA.distance(pointB, 'L2')
        AC = pointA.distance(pointC, 'L2')
        BC = pointB.distance(pointC, 'L2')

        half_circumference = (AB + BC + AC) / 2

        area_heron = sqrt(half_circumference*(half_circumference - AB)*(half_circumference - AC)*(half_circumference - BC))
        return area_heron

    # User height
    def triangle_area_height(pointA, pointB, pointC):
        AB = pointA.distance(pointB, 'L2')
        lineAB = Line.line_pass_two_point(pointA, pointB)
        distance_from_C_to_AB = lineAB.distance_from_point_to_line(pointC)
        area_height = (AB*distance_from_C_to_AB) / 2
        return area_height


if __name__ == '__main__':
    pointA = Point(1, 3)
    pointB = Point(-5, 6)
    pointC = Point(0, 1)
    print(Triangle.triangle_area_heron(pointA, pointB, pointC)) #7,5
    print(Triangle.triangle_area_height(pointA, pointB, pointC)) #7,5
