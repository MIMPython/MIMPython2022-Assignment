"""
Cho phương trình y = ax + b với a,b là các tham số bất kì.
Nhận xét: Đường thẳng mô tả bởi phương trình trên có vector chỉ phương là (a,-1) với 
a là số thực bất kì. Để chỉ ra rằng đây không phải là phương trình tổng quát của
đường thẳng trong không gian \mathbb{R}^2, ta cần chỉ ra một đường thẳng mà không có 
vector pháp tuyến dưới dạng (a,-1) với mọi a \in \mathbb{R}. Đường thẳng đó là 
x = 0.
"""
"""
Cho phương trình ax + by + c = 0.
Để phương trình nói trên là phương trình tổng quát của một đường thẳng trong 
\mathbb{R}^2 thì a,b phải không đồng thời bằng 0.
"""
import numpy as np
import math


#initializing a class
class Line:
    def __init__(self,name, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = name

#extrating information from the Cartesian equation of a line
    def call_a(self):
        return self.a
    def call_b(self):
        return self.b
    def call_c(self):
        return self.c
# define a function that construct a line
    def line_constructing(self):
        cartesian_equation = f"{self.a}x + {self.b}y + {self.c} = 0"
        if self.a == self.b == 0:
            print("Invalid input, no such line exists")
        else:
            print(f"The Cartesian coordinate of the {self.name} is",\
                f"{cartesian_equation}")
#find the intersection between two lines on a plane
    def intersect(self, other):
        coefficient_matrix = np.array([[self.a,self.b],[other.a,other.b]])
        rank_coefficient_matrix = np.linalg.matrix_rank(coefficient_matrix)
        augmented_matrix = np.array([[self.a,self.b,- self.c],[other.a,other.b,- other.c]])
        rank_augmented_matrix = np.linalg.matrix_rank(augmented_matrix)

        if self.a == self.b == 0 or other.a == other.b == 0:
            print(f'There exists an invalid input')

        elif rank_coefficient_matrix == rank_augmented_matrix == 2:
                coefficient_matrix_1 = np.array([[- self.c,self.b],[- other.c,other.b]])
                coefficient_matrix_2 = np.array([[self.a,- self.c],[other.a,- other.c]])
                x_1 = (np.linalg.det(coefficient_matrix_1))/(np.linalg.det(coefficient_matrix))
                x_2 = (np.linalg.det(coefficient_matrix_2))/(np.linalg.det(coefficient_matrix))

                print(f'The intersection of {self.name} and {other.name} is ({x_1},{x_2})')

        elif rank_coefficient_matrix == 1:
            print(f'{self.name} and {other.name} are parallel to each other')

        elif rank_coefficient_matrix != rank_augmented_matrix:
            print(f'{self.name} and {other.name} do not intersect')

#importing a class from another file
from week04_assignment02_student09_DinhTienDat import Point

#distance between a point and a line
def my_distance(x,y,a,b,c):
    return (abs(a*x + b*y + c))/(math.sqrt(a**2 + b**2))

#code testing
A = Point('O',0,0)
valid_line = Line('valid line',1,1,2)
invalid_line = Line('none', 0,0,3)
x_axis = Line('x axis',0,1,0)
y_axis = Line('y axis',1,0,0)
valid_line.line_constructing()
invalid_line.line_constructing()
x_axis.line_constructing()

valid_line.intersect(invalid_line)
valid_line.intersect(x_axis)
result = my_distance(A.read_x(),A.read_y(),x_axis.call_a(),x_axis.call_b(),x_axis.call_c())
print(f'distance between point O and the x axis is {result}')