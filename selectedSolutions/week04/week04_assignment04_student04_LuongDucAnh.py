from week04_assignment02_student04_LuongDucAnh import Point
from week04_assignment03_student04_LuongDucAnh import Line

def getArea(A: Point, B: Point, C: Point):
    a = B.distance(C, "L2") #Base
    BC = Line.lineFromPoints(B, C) #Create a line from 2 point 
    h = BC.getDistance(A) #Height
    return a*h/2 #Area of Triangle

def main():
    A = Point(2, -1)
    B = Point(1, 2)
    C = Point(2, -4)
    print(getArea(A, B, C)) #1.5
    
if __name__ == "__main__":
    main()