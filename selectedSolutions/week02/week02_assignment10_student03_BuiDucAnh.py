from matplotlib import pyplot as plt
import math as m
import numpy as np
def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4 * a * c
    tup = ()
    if delta == 0:
        tup += (-b / (2 * a) ,)
    if delta > 0:
        tup += ((-b + m.sqrt(delta) ) / (2 * a) ,)
        tup += ((-b - m.sqrt(delta) )/ (2 * a) ,)
    return tup
def triangle(A, B, C):
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        plt.figure()
        plt.xlabel('Horizontal axis', fontsize = 16)
        plt.ylabel('Vertical axis', fontsize = 16)
        plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1])
def equilateral_polygon (coordinate_A, coordinate_B):
    x1, y1 = coordinate_A
    x2, y2 = coordinate_B
    r = (x1 - x2)**2 + (y1 - y2)**2
    xM = (x1 + x2)/2
    yM = (y1 + y2)/2
    vec1 = x2 - x1
    vec2 = y2 - y1
    a = (vec1 * xM + vec2 * yM) / vec2
    b = - vec1 / vec2
    A = b**2 + 1
    B = 2 * a * b - 2 * x1 - 2 * y1 * b
    C = a**2 - 2 * y1 * a - r + x1**2 + y1**2
    xC1 , xC2 = solve_quadratic_equation(A, B, C)
    yC1 = a + b * xC1
    yC2 = a + b * xC2
    tup = ()
    tup1 = ()
    tup2 = ()
    tup1 += (xC1, yC1)  
    tup2 += (xC2, yC2)
    tup += (tup1, tup2) 
    return tup
coorA = tuple(map(int ,input('Enter your first co-ordinate: ').split()))
coorB = tuple(map(int ,input('Enter your second co-ordinate: ').split()))
coorC1, coorC2 = equilateral_polygon (coorA, coorB)
print('Valid co-ordinates for C: ', equilateral_polygon (coorA, coorB))
triangle(coorA, coorB, coorC1)
triangle(coorA, coorB, coorC2)
plt.show()