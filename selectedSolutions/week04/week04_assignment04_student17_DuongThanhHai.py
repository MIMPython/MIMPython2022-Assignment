
from sympy import *
import math
from week04_assignment02_student17_DuongThanhHai import Point

A = Point(1,-5)
B = Point(2,1)
C = Point(13,-8)

#cachs 1
def Area (A, B, C):
    S = (1/2) * abs( (B.x-A.x)*(C.y-A.y) - (C.x-A.x)*(B.y-A.y) )
    return S

S1 = Area (A,B,C)
print ('cach 1 = ' + str(S1))

#cach 2
AB = Point.distance(A,B)
BC = Point.distance(B,C)
AC = Point.distance(A,C)

p = (AB + BC + AC)/2

S2 = math.sqrt( p*(p-AB)*(p-AC)*(p-BC) )

print ('cach 2 = ' + str(S2))











