from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y


    #Method to get distance between 2 points in L1 (Mahatann) or L2 (Euclid)
    def distance(self, point, metric):
        if metric == 'L1':
             return abs(self.x - point.getX()) + abs(self.y -  point.getY())
        elif metric == 'L2':
            return sqrt((self.x - point.getX())**2 + (self.y -  point.getY())**2)
        else:
            return "Invalid metric"
        
    #Method to get a symetry point of entry point
    def symmetryPoint(self):
        return Point(-self.getX(), -self.getY())
    
    def __repr__(self):
        return '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
    
    
if __name__ == '__main__':
    pointA = Point(0,0)
    pointB = Point(1,2)
    pointC = Point(5,4)
    
    print(pointA)
    print(pointA.distance(pointB,"L2"))
    print(pointB.distance(pointC, "L1"))
    print(pointC.symmetryPoint())
    
"""
    results:
        (0,0)
        2.236067977499796
        6
        (-5,-4)
"""