from week04_assignment02_student33_HoangNhatMinh import Point
from week04_assignment03_student33_HoangNhatMinh import Line

A = Point(0, 0)
B = Point(0, 2)
C = Point(2, 0)
AB = Line.constructor(A, B)

S = AB.distanceTo(*C.__dict__.values()) * A.distanceTo('L2', *B.__dict__.values()) / 2

print("Area of triangle ABC is: " + str(S))
