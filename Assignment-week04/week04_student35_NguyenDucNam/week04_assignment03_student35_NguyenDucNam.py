from math import *
from week04_assignment02_student35_NguyenDucNam import Point

class Line:
    """Câu a: Phường trình đường thẳng có dạng y = ax + b với a,b là 2 tham số bất kì không phải là phương trình tổng quát của một đường thằng trong mặt phẳng Oxy vì nó không thể hiện đường thẳng x = ? """
    """Câu b: Để phương trình ax + by + c = 0 là phương trình tổng quát của đường thẳng thì a,b phải khác 0"""
    
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
        result = abs(self.a *x + self.b*y + self.c)/ sqrt(self.a**2 + self.b**2)
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
           

if __name__ == '__main__':
    LineA = Line(1,1,-1)
    LineB = Line(1,1,-1)
    print("Import A:")
    x1 = int(input('x1= '))
    y1 = int(input('y1= '))
    print('Import B:')
    x2 = int(input('x2= '))
    y2 = int(input('y2= '))
    print(LineA.intersectionOfLines(LineB))     #Show intersection of LineA and LineB
    print(LineA.distanceOfPointAndLine(x1,y1))  #Calculate the distance of A and LineA
    print(Line.getLineOfTwoPoints(x1,y1,x2,y2)) #Get line witH A and B

        