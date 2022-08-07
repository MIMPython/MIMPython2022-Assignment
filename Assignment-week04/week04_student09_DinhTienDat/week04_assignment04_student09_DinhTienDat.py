import math
from week04_assignment02_student09_DinhTienDat import Point

A = Point('A',1,1)
B = Point('B',2,3)
C = Point('C',1,4)

#Coefficients of the equation of the line BC
BC_coefficient_a = C.read_y() - B.read_y()
BC_coefficient_b = B.read_x() - C.read_x()
BC_coefficient_c = (C.read_x() * B.read_y()) - (B.read_x() - C.read_y()) 

#distance between a point and a line
def my_distance(x,y,a,b,c):
    return (abs(a*x + b*y + c))/(math.sqrt(a**2 + b**2))

height = my_distance(A.read_x(),A.read_y(),BC_coefficient_a, \
BC_coefficient_b,BC_coefficient_c)
area = (1/2)* height * (math.sqrt((B.read_x() - C.read_x())**2 \
    +(B.read_y() - C.read_y())**2))

A.read_coordinate()
B.read_coordinate()
C.read_coordinate()
print(f"The area of the triangle ABC is {round(area,2)}")
