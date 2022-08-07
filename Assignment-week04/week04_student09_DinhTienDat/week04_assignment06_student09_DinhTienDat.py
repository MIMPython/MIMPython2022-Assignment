import math

class Circle:
    def __init__(self,name, a, b, r):
        self.name = name
        self.a = a
        self.b = b
        self.r = r

    def circ_construct(self):
        equation = f'(x - {self.a})^2 + (y - {self.b})^2 = {self.r ** 2} '
        print(f'The Cartesian equation of {self.name} is {equation}')

circ = Circle('the circle center at (0,1) with radius = 2', 0, 1, 2)
circ.circ_construct()