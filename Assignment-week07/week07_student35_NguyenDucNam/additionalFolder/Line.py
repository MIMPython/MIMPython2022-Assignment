from .Point import Point
import math
class Line:
    
    def __init__(self,a,b,c):
        """Initialize attributes to a line"""
        self.a = a
        self.b = b
        self.c = c
        
    def intersectionOfLines(self,other):
        """Show the intersection of two lines"""

        D = self.a*other.b - other.a*self.b
        Dx = other.b*self.c - self.b*other.c
        Dy = self.a*other.c - other.a*self.c

        #have a root
        if D != 0:  
            x = round(Dx/D,2)
            y = round(Dy/D,2)
            return (x,y)

        #infinite roots    
        elif Dx==0 and Dy == 0:
            return (0,0)

        #no roots    
        else: 
            return ()

    def distanceOfPointAndLine(self,x,y):
        """Calculate distance of a point and a line"""
        self.point = Point(x,y)
        result = abs(self.a *x + self.b*y + self.c) / math.sqrt(self.a**2 + self.b**2)
        return result

    @classmethod
    def getLineOfTwoPoints(cls,x1,y1,x2,y2):
        """Show attributes of a line which contains two points"""
        cls.pointA = Point(x1,y1)
        cls.pointB = Point(x2,y2)
        cls.a = y2 - y1
        cls.b = -(x2 - x1)
        cls.c = -(cls.a*x1 + cls.b*y1)
        return (cls.a,cls.b,cls.c)

    
           