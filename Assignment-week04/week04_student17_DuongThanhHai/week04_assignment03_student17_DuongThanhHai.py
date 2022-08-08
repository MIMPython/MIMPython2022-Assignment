
import math
from week04_assignment02_student17_DuongThanhHai import Point

# ax + by + c = 0

class Line:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def lineIntersection (line01, line02):
        D = line01.a * line02.b - line02.a * line01.b
        D1 = line01.c * line02.b - line01.b * line02.c 
        D2 = line01.a * line02.c - line01.c * line02.a

        if D == D1 == D2 == 0:
            print ('2 duong thang trung nhau')

        elif (D == 0 & D1 != 0) or (D == 0 & D2 !=0):
            return tuple()
        
        elif D != 0:
            x = D1/D
            y = D2/D

            return (x,y)

    def line_and_point(point, line):
        d = abs(line.a*point.x + line.b*point.y + line.c) / math.sqrt(line.a**2 + line.b**2)
        return (d)

    def makeLine (point01, point02):
        Ny = - (point01.x - point02.x)
        Nx = point01.y - point02.y
        # n = (Uy, -Ux)

        c = -(Nx*point01.x + Ny*point01.y)

        return (str(Nx) + 'x + ' + str(Ny) + 'y + ' + str(c) + '=0')


    
if __name__ == '__main__':
    line01 = Line(3,-4,-15)
    line02 = Line(5,2,1)
    point01 = Point(1,2)
    point02 = Point(3,-1)

    x = Line.lineIntersection(line01, line02)
    print (x)

    y = Line.line_and_point(point01, line01)
    print (y)

    z = Line.makeLine(point01, point02)
    print (z)





    