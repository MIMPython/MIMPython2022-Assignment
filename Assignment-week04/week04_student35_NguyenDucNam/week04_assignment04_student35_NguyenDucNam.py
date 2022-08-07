from week04_assignment02_student35_NguyenDucNam import Point
from week04_assignment03_student35_NguyenDucNam import Line
from math import *

print('Import A:')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
print('Import B:')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
print('Import C:')
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))

#Get the linear equation of BC
equationBC = Line.getLineOfTwoPoints(x2,y2,x3,y3)

#Create line BC with attributes in class Line
LineBC = Line(equationBC[0],equationBC[1],equationBC[2])

#Calculate the length of line BC
BC = sqrt((x3-x2)**2 + (y3-y2)**2)

#Calculate the high of triangle ABC
h = LineBC.distanceOfPointAndLine(x1,y1)

#Calculate the area of triangle ABC
S = h * BC / 2

print('The area of triangle ABC is:',S)

        