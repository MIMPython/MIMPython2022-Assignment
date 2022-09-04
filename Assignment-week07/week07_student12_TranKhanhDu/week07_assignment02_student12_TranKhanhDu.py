class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @classmethod
    def introduce(cls):
        return f'this is {cls.__name__}'
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def introduce(cls, length, width):
        return super().introduce(cls, length, width)
    def area(self):
        return super().area()
    def perimeter(self):
        return super().perimeter()

#rhombus and rectangle are two different kind of graph so we can't extend rectangle for rhombus 
rectangle = Rectangle(9,6)
print(rectangle.area())
print(rectangle.introduce())
square = Square(9,9)
print(square.perimeter())

class Eclipse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calPerimeter(self,)

