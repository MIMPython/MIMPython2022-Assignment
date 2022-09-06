'''
Bài tập 2. (class inheritance)
1) Xây dựng class Rectangle và class Square (kế thừa từ Rectangle). Thiết kế các thuộc tính, phương thức có liên quan.
1) Bổ sung thêm class Rhombus và thực hiện kế thừa một cách phù hợp.
2) Thực hiện yêu cầu tương tự với class Ellipse và class Circle. Chú ý rằng việc tính chu vi hình ellipse là một bài toán thú vị.
'''
import math
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def getArea(self):
            return self.length * self.width
            
        
    def getPerimeter(self):
            return (self.length + self.width) * 2
             

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Rhombus(Rectangle):
    def __init__(self, length, width, side):
        self.side = side

    def getArea(self):
         return (self.length * self.width)/2

    def getPerimeter(self):
         return self.side * 4

class Ellipse(Rectangle):
    def __init__(self, truc_lon, truc_be):
        self.truc_lon = truc_lon
        self.truc_be = truc_be
    
    def getArea(self):
         return math.pi * (self.truc_lon/2) * (self.truc_be/2)

    def getPerimeter(self):
         return math.pi * ( 3*(self.truc_lon/2 + self.truc_be/2) - math.sqrt( (3*self.truc_lon + self.truc_be) * (self.truc_lon + 3*self.truc_lon) ) )

class Circle(Ellipse):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
         return math.pi * (self.radius ** 2)
    
    def getPerimeter(self):
         return 2 * math.pi * self.radius

if __name__ == '__main__':
    rectangle = Rectangle(4, 5)
    square = Square(4)
    rhombus = Rhombus(4, 5, 3)
    area_1 = rectangle.getArea()
    area_2 = square.getArea()
    perimeter_1 = rhombus.getPerimeter()
    print(area_1) # 20 
    print(area_2) # 16
    print(perimeter_1) # 12 

