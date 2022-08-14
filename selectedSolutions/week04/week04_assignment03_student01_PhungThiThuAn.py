# a, Phương trình đường thẳng có dạng y=ax+b với a,b là hai tham số bất kỳ không phải là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy vì trường hợp đường thẳng có dạng: x = c (với c là 1 hằng số bất kì) thì không biểu diễn được qua phương trình này.
# b, Điều kiện của 3 tham số a, b, c để phương trình này là phương trình tổng quát của 1 đường thẳng là: a và b không cùng bằng 0.
# c, Đoạn code nên có thêm comment.

from week04_assignment02_student01_PhungThiThuAn import Point


class Line:
    '''
    Creates a line in Oxy plane
    '''
    def __init__(self, a, b, c):
        '''
        Defines a, b, c variables
        
        '''
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f'{self.a}x + {self.b}y + {self.c} = 0'

    @classmethod
    def initializeByPoints(cls, pointA, pointB):
        '''
        Create a Line object by 2 points.
        
        '''
        cls.a = pointA.y - pointB.y
        cls.b = pointB.x - pointA.x
        cls.c = - cls.a*pointA.x - cls.b*pointA.y
        return Line (cls.a, cls.b, cls.c)
        
    def isValidLine(self):
        # condition: a != 0 and b!= 0
        return self.a** 2 + self.b**2 != 0 

    def printIntersection(self, other):
        if self.isValidLine() and other.isValidLine():
            if self.a*other.b == self.b*other.a:
                # 2 lines are parallel
                if self.b*other.c != self.c*other.b:
                    return ()
                # 2 lines are coincide
                else:
                    x = 1.0
                    y = (-self.c - self.a)/self.b
                    return (Point(x, y))
            # 2 lines are intersecting
            else:
                if self.b == 0:
                    x = -self.c/self.a
                    y = (- other.a*x - other.c) / other.b
                    return (Point(x, y))
                elif other.b == 0:
                    x = -other.c/other.a
                    y = (- self.a*x - self.c) / self.b
                    return (Point(x, y))
                else:
                    x = (other.c/other.b - self.c/self.b)/(self.a/self.b - other.a/other.b)
                    y = (- self.a*x - self.c) / self.b
                    return (Point(x, y))
                
        else:
            pass

    def distaneToAPoint(self, point):
        distance = abs(self.a*point.x + self.b*point.y +self.c) / (self.a**2 + self.b**2)**(1/2)
        return round(distance, 3)

if __name__ == '__main__':
    line1 = Line(1, 1, 3)
    print(line1) # 1x + 1y + 3 = 0
    line2 = Line(0, 1, 3)
    print(line1.printIntersection(line2)) #(0.0,-3.0)

    line3 = Line(1, 1, 3)
    line4 = Line(1, 1, 3)
    print(line3.printIntersection(line4)) #(1.0,-4.0)

    line5 = Line(1, 1, 3)
    line6 = Line(1, 1, -3)
    print(line5.printIntersection(line6)) #()

    print(line1.distaneToAPoint(Point(2, 3))) # 5.657
    O = Point(0, 0)
    print(line2.distaneToAPoint(O)) # 3.0

    print(Line.initializeByPoints(Point(3, 4), Point(1, 0))) # 4x + -2y + -4 = 0