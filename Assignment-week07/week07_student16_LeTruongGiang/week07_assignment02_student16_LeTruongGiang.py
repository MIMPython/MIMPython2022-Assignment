import math

'''
1
'''
print('(1)')
class Rectangle:
    nSides = 4

    @classmethod
    def hello(cls):
        print(f'This is a method defined in class Rectangle.')
        print(f'Hello from {cls.__name__}!')


class Square(Rectangle):
    pass

Rectangle.hello()
print(f'Sides: {Rectangle.nSides}')
Square.hello()
print(f'Sides: {Square.nSides}')

print('\n',end='\n')

'''
1'
'''

print("(1')")
class Rhombus:
    nSides = 4
    
    @classmethod
    def hello(cls):
        print(f'This is a method defined in class Rhombus.')
        print(f'Hello from {cls.__name__}!')
        
class Rectangle(Rhombus):
    pass
class Square(Rhombus):
    pass

Rhombus.hello()
print(f'Sides: {Rhombus.nSides}')
Rectangle.hello()
print(f'Sides: {Rectangle.nSides}')
Square.hello()
print(f'Sides: {Square.nSides}')

print('\n',end='\n')


'''
2
'''
print("(2)")

class Elipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def perimeter(self):
        p = math.pi*(self.a + self.b)
        return p

class Circle(Elipse):
    def __init__(self, a, b):
        super.__init__(a,b)
    
    def checkCircle(self):
        if self.a == self.b: 
            return True
        return False


elipse1 = Elipse(2,2)

def perimeter_cal(obj):
    if Circle.checkCircle(obj) == True:
        print(f'{obj.a}, {obj.b}\nThe perimeter of the CIRLCE is {obj.perimeter()}')
    else:
        print(f'a = {obj.a}, b = {obj.b}\nThe perimeter of the ELIPSE is {obj.perimeter()}')
        
perimeter_cal(elipse1)

    