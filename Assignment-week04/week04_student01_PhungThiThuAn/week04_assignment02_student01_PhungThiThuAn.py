import math

class Point:
    '''
    Creates a point on a coordinate plane with values x and y.
    
    '''
    def __init__(self, x, y):
        '''
        Defines x and y variables
        
        '''
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def setX(self, x):
        self.x = x
   
    def setY(self, y):
        self.y = y

    def setPoint(self, x, y):
        self.x = x
        self.y = y

    '''
    Function in 2.2
    
    '''
    # def distance(self, other):
    #     dx = self.x - other.x
    #     dy = self.y - other.y
    #     return math.sqrt(dx**2 + dy**2)

    '''
    Function in 2.3
    
    '''
    def distance(self, other, metric='L2'):
        dx = self.x - other.x
        dy = self.y - other.y
        if metric == 'L2':
            return round(math.sqrt(dx**2 + dy**2), 2)
        elif metric == 'L1':
            return abs(dx) + abs(dy)

    def getOSymmetricPoint(self):
        # Solution 2 of 2.4
        return Point(-self.x, -self.y)
        
    def __symmetry__(self):
        return self.__class__(-self.x, -self.y)
    
    def __repr__(self) -> str:
        return f'Point: ({self.x},{self.y})'


def O_symmetricPoint(point):
    '''
    Solution 1 of 2.4
    point: a point on a coordinate plane with values x and y.
    
    '''
    return Point(-point.x, -point.y)

if __name__ == '__main__':
    # Output below
    pointA = Point(4, 2)
    print('pointA:',pointA)
    pointA.setPoint(4, 5)
    print('new pointA:', pointA)
    pointB = Point(1, 0)
    pointB.setX(12)
    pointB.setY(14)
    print('pointB:', pointB)
    distL1 = pointA.distance(pointB, metric = 'L1')
    distL2 = pointA.distance(pointB, metric = 'L2')
    print(distL1, distL2)
    print('Test 3 functions to return a new point which symmetry with pointA')
    print(O_symmetricPoint(pointA))
    print(pointA.getOSymmetricPoint())
    print(pointA.__symmetry__())
    print(repr(pointB))

'''
This is output
pointA: (4,2)
new pointA: (4,5)
pointB: (12,14)
17 12.04
Test 3 functions to return a new point which symmetry with pointA
(-4,-5)
(-4,-5)
(-4,-5)
Point: (12,14)
'''


