import math
from week04_assignment02_student23_HuaQuangHuy import Point

if __name__ == '__main__':
    # 3 diem in Oxy
    pointA = Point(0, 0)
    pointB = Point(0, 5)
    pointC = Point(6, 0)

    # get length of 3 edge of triangle
    edgeAB = pointA.distance(pointB)
    edgeBC = pointB.distance(pointC)
    edgeCA = pointC.distance(pointA)

    # get area of triangle by heron formular
    p = (edgeAB + edgeBC + edgeCA) / 2
    area = math.sqrt(p * (p - edgeAB) * (p - edgeBC) * (p - edgeCA))
    print(f"area of triangle is {area}")  # area of triangle is 15.0
