import numpy as np
# Bài tập 2. (class inheritance)
# 1) Xây dựng class Rectangle và class Square (kế thừa từ Rectangle). Thiết kế các thuộc tính, phương thức có liên quan.
# 1’) Bổ sung thêm class Rhombus và thực hiện kế thừa một cách phù hợp.
# 2) Thực hiện yêu cầu tương tự với class Ellipse và class Circle. Chú ý rằng việc tính chu vi hình ellipse là một bài toán thú vị.
class Rhombus:
    def __init__(self, length, width, angle = np.pi / 6 ,center = (0, 0)):
        self.length = length
        self.width = width
        self.angle = angle
        self.center = center

    @property        
    def area(self):
        return self.length * self.width * np.sin(self.angle)
    
    @property        
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    @property
    def diagonal(self):
        return np.sqrt(self.width ** 2 + self.length ** 2 - 2 * self.width * self.length * np.cos(self.angle))

    def __str__(self):
        return f"Length: {self.length}, width: {self.width}"


class Rectangle(Rhombus):
    
    def __init__(self, length, width, angle = np.pi / 2, center = (0, 0)):
        super().__init__(length, width, angle, center)
    
    @property        
    def area(self):
        return self.length * self.width

    @property
    def diagonal(self):
        return np.sqrt(self.width ** 2 + self.length ** 2)

class Square(Rectangle):
    
    def __init__(self, side,  angle = np.pi / 2, center = (0, 0)):
        super().__init__(side, side, angle, center)

    def __str__(self):
        return f"Side: {self.width}"      

# -----------------------------------------------------------------------------------------------------

class Ellipse:
    def __init__(self, semi_major_axes, coordinate_foci_1 = (-1, 0), center = (0, 0)):
        self.semi_major_axes = semi_major_axes             # bán trục lớn
        self.coordinate_foci_1 = coordinate_foci_1         # Tiêu điểm thứ 1
        self.center = center

    @property
    def focal_distance(self):                              # Bán tiêu cự
        return np.sqrt((self.center[0] - self.coordinate_foci_1[0]) ** 2 + (self.center[1] - self.coordinate_foci_1[1]) ** 2)

    @property
    def coordinate_y_foci_2(self):                         # Tiêu điểm thứ 2
        return (2 * self.focal_distance + self.coordinate_foci_1[0], 2 * self.focal_distance + self.coordinate_foci_1[1])

    @property
    def semi_minor_axes(self):                             # Bán trục nhỏ       
        return np.sqrt(self.semi_major_axes ** 2 -  self.focal_distance ** 2)
    
    @property
    def area(self):
        return np.pi * self.semi_major_axes * self.semi_minor_axes
    
    def __str__(self):
        return f'Phương trình hình ellipse : x^2 / {self.semi_major_axes}^2 + y^2 / {self.semi_minor_axes}^2 = 1.'

class Circle(Ellipse):
    def __init__(self, semi_major_axes, center = (0, 0)):
        super().__init__(semi_major_axes, center, center)


a = Ellipse(10, (-2, 0) , (2, 3))
print(a.center)
print(a.coordinate_foci_1)
print(a.focal_distance)
print(a.coordinate_y_foci_2)
print(a.semi_minor_axes)
print(a)






