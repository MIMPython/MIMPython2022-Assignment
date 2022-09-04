import math

from .point import Point
class Circle:
    def __init__(self, center:Point, radius):
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"
    
    def getPerimeter(self):
        return 2*math.pi*self.radius
    
    def getArea(self):
        return math.pi*self.radius**2