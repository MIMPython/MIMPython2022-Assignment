"""
    a) y = ax + b không là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy vì nó không biểu diễn được mọi đường thẳng trong mặt phẳng Oxy
    Có thể ví dụ như đường thẳng x = -1, x = 2,...
    b) Để ax + by + c = 0 là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy thì a, b không đồng thời bằng 0
    c) Đoạn code chưa loại bỏ trường hợp không vẽ được đường thẳng, hay là a = b = 0
"""
from week04_assignment02_student04_LuongDucAnh import Point
import math

class Line:
    def __new__(cls, a, b, c):
        if a**2 + b **2 != 0:
            obj = super().__new__(cls)
            obj.a, obj.b, obj.c = a, b, c
            print ("The line has been initialized")
            return obj
        else:
            print ("Invalid line, a and b are not all simultaneously equal to zero")
            return None

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"
        
    def findLineIntersection(self, other):
        det = self.a * other.b - other.a * self.b
        if det == 0:
            if self.b != 0:
                if other.a + other.b * (-self.c - self.a)/self.b == -other.c:
                    return "infinite roots"
            elif self.a != 0:
                if other.b + other.a * (-self.c - self.b)/self.a == -other.c:
                    return "infinite roots"
            return ()
        else:
            x = (other.b * (-self.c) - self.b * (-other.c))/det
            y = (self.a * (-other.c) - other.a * (-self.c))/det
            return (Point(x, y),)
    
    def getDistance(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c)/math.sqrt(self.a**2 + self.b**2)
    
    @classmethod
    def lineFromPoints(cls, A, B):
        a = B.y - A.y
        b = A.x - B.x
        c = -a * A.x - b * A.y
        return cls(a, b, c)
    
def main():
    M = Point(1, -1)
    d = Line(3, -4, -21)
    d1 = Line(3, -4, 5)
    d2 = Line(3, -4, -21)
    d3 = Line(4, 7, 9)
    print(d.getDistance(M)) #2.8
    print(d.findLineIntersection(d1)) #()
    print(d.findLineIntersection(d2)) #infinite roots
    print(d.findLineIntersection(d3)) #(Point(3.0, -3.0),)
    
if __name__ == "__main__":
    main()