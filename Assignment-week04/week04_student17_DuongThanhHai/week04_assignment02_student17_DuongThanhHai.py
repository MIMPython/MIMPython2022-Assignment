
import math

class Point:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance( point_01, point_02):
        dis = math.sqrt( ((point_01.x - point_02.x)**2) + ((point_01.y - point_02.y)**2) )

        return dis

    def doi_xung (point):
        x2 =  - point.x
        y2 =  - point.y
        return (x2, y2)
        

if __name__ == '__main__':
    #instance
    A = Point(2,3)
    B = Point(-5,-1)
    C = Point(3,-4)

    #distance
    x = Point.distance(A,B)
    print (x)

    #doi_xung
    y = Point.doi_xung(A)
    print (y)




