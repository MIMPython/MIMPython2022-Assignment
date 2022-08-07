from week04_assignment02_student24_NguyenKhanhHuyen import Point
from week04_assignment03_student24_NguyenKhanhHuyen import Line
import math

def Area(pA, pB, pC):
    lineAB_len = pA.distance(pB, metric = 'L1')
    lineBC_len = pB.distance(pC, metric = 'L1')
    lineAC_len = pC.distance(pA, metric = 'L1')
    P = (lineAB_len + lineBC_len + lineAC_len)/2
    res = math.sqrt(P*(P-lineAB_len)*(P-lineAC_len)*(P-lineBC_len))
    return res

if __name__ == '__main__':
    pointA = Point(0, 1)
    pointB = Point(1, -2)
    pointC = Point(2, 0)
    print((Area(pointA, pointB, pointC)))