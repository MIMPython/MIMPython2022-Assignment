from math import pi, sqrt

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def getArea(self):
        return self.height*self.width

    def getPerimeter(self):
        return 2*(self.height+self.width)

    def __repr__(self) -> str:
        return f'Rectangle[width = {self.width}, height = {self.height}, area = {self.getArea():.3f}, perimeter = {self.getPerimeter():.3f}]'

class Square(Rectangle):
    def __init__(self, side) -> None:
       super().__init__(side, side)

    def __repr__(self) -> str:
        return f'Square[side = {self.width}, area = {self.getArea():.3f}, perimeter = {self.getPerimeter():.3f}]'

class Rhombus(Rectangle):
    '''
    width and height is length of 2 diagonals 
    '''
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    def getArea(self):
        return super().getArea()/2

    def getPerimeter(self):
        return 2*(sqrt(self.width**2+self.height**2))

    def __repr__(self) -> str:
        return f'Rhombus[width = {self.width}, height = {self.height}, area = {self.getArea():.3f}, perimeter = {self.getPerimeter():.3f}]'

rectangle = Rectangle(3, 7)
square = Square(2)
rhombus = Rhombus(2, 3)
print(rectangle) # Rectangle[width = 3, height = 7, area = 21.000, perimeter = 20.000]
print(square) # Square[side = 2, area = 4.000, perimeter = 8.000]
print(rhombus) # Rhombus[width = 2, height = 3, area = 3.000, perimeter = 7.211]   


# part 2
class Ellipse:
    '''
    a: semi-major
    b: semi-minor axes

    '''    
    def __init__(self, a, b) -> None:
        if a > b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def getArea(self):
        return pi*self.a*self.b

    def getCircumference(self):
        diffAB = self.a-self.b
        sumAB = self.a+self.b
        h = (diffAB/sumAB)**2
        return pi*sumAB*(1+(3*h/(10+sqrt(4-3*h))))

class Circle(Ellipse):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius)

ellipse = Ellipse(5, 2)
circle = Circle(6)
print(ellipse.getArea())
print(circle.getCircumference())
# 31.41592653589793
# 37.69911184307752