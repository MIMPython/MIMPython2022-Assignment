import math

class Point:
    """Initialize a simple class to calculate distance"""
    def distance(pointA, pointB, metric):
        if ( metric == 'L1'):
            distL1 = abs( pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])
        else: 
            distL1 = math.sqrt(( pointA[0] - pointB[0])**2 + ( pointA[1] - pointB[1])**2)
        print("khoảng cách giữa 2 điểm là: ", distL1, sep="")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None

    def getSomething(pointA):
        print("Điểm cần tìm là: (", -pointA[0], "; ", -pointA[1], ")", sep ="")


A = [1, 2]
B = [3, 4]
Point.distance(A, B, "L1") 
Point.distance(A, B, "L2") 
Point.getSomething(A) #tìm  điểm đối xứng với A qua gốc O