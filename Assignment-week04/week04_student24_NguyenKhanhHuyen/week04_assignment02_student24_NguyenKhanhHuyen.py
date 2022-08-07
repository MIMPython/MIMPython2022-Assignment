from dis import dis
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    def __repr__(self): 
       return '(%s, %s)' % (self.x, self.y)

    def distance(self,pB,metric):
        if metric == "L1":
            dis = math.sqrt((self.x - pB.x)**2+(self.x-pB.y)**2)
        if metric == "L2":
            dis = abs(self.x-pB.x)+abs(self.y - pB.y)
        return dis
def symmetryPoint(pA):
    newPoint = Point(-(pA.x), -(pA.y))
    return newPoint
if __name__ == '__main__':
    pointA = Point(4, 2)
    pointB = Point(5, 6)
    print(pointA)
    print(pointA.distance(pointB, metric = 'L1')) #2.236...
    print(symmetryPoint(pointA))
