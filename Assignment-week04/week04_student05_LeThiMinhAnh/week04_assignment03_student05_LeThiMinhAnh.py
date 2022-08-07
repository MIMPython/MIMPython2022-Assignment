# a) Vì sao phương trình đường thẳng có dạng y=ax+b với a,b là hai tham số bất kỳ không phải là phương trình tổng quát của một
# đường thẳng trong mặt phẳng Oxy? Đường thẳng nào không biểu diễn được qua phương trình này?
# Vì phương trình này không biểu diễn được đường thẳng x = c (c là tham số bất kì)
#
# b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ.
# Tìm điều kiện của ba tham số a,b,c để phương trình này là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy.
# Điều kiện: a**2 + b**2 !=0, c bất kì
#
#  c) Phần khởi tạo của class Line có thể được viết như sau
# class Line:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
# Nhận xét đoạn code trên: Đã khởi tạo được đủ tham số yêu cầu của một đường thẳng, nhưng
# cần thêm điều kiện ràng buộc để đảm bảo hai tham số a và b không thể đồng thời bằng 0
from week04_assignment02_student05_LeThiMinhAnh import Point
from math import lcm, sqrt


class ValueException(Exception):
    def __init__(self, value):
        self.value = value


class Line:
    def __init__(self, a, b, c):
        if a == 0 and b == 0:
            raise ValueException("a and b not both equal to zero")
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return "Line %sx + %sy + %s = 0 " % (self.a, self.b, self.c)

    def get_intersections(self, delta):
        if self.a == 0 and delta.a == 0 or self.b == 0 and delta.b == 0:
            if self.c == delta.c:
                print("Two lines are coincident")
                return self
            else:
                print("Two lines are parallel")
                return ()
        elif self.a == 0 and delta.b == 0:
            print("Two lines are intersecting at exactly one point:")
            return Point(-delta.c/delta.a, -self.c/self.b)
        elif self.b == 0 and delta.a == 0:
            print("Two lines are intersecting at exactly one point:")
            return Point(-self.c/self.a, -delta.c/delta.b)
        elif self.a == 0 and delta.a != 0:
            print("Two lines are intersecting at exactly one point:")
            return Point((-delta.c+self.c/self.b*delta.b)/delta.a, -self.c/self.b)
        elif self.a != 0 and delta.a == 0:
            print("Two lines are intersecting at exactly one point:")
            return Point((-self.c+self.b*delta.c/delta.b)/self.a, -delta.c/delta.b)
        elif self.a != 0 and delta.a != 0:
            alpha = lcm(self.a, delta.a)/self.a*self.b - \
                lcm(self.a, delta.a)/delta.a*delta.b
            beta = (lcm(self.a, delta.a)/self.a*self.c -
                    lcm(self.a, delta.a)/delta.a*delta.c)
            if alpha != 0:
                print("Two lines are intersecting at exactly one point:")
                return Point(-self.c-self.b*(-beta)/alpha, -beta/alpha)
            else:
                if beta != 0:
                    print("Two lines are parallel")
                    return ()
                else:
                    print("Two lines are coincident")
                    return self

    def point_line_distance(self, point):
        return abs(self.a*point.x + self.b*point.y+self.c)/sqrt(self.a**2+self.b**2)

    @classmethod
    def lineFromPoints(cls, pointA, pointB):
        a = pointA.y - pointB.y
        b = pointB.x - pointA.x
        c = -a*pointA.x - b*pointA.y
        return cls(a, b, c)


if __name__ == '__main__':
    line1 = Line(0, 2, 5)
    line2 = Line(1, 3, 1)
    print(repr(line1))  # Line 0x + 2y + 5 = 0
    print(repr(line2))  # Line 1x + 3y + 1 = 0
    print(line1.get_intersections(line2))
    # Two lines are intersecting at exactly one point
    # Point(6.5, -2.5)
    pointA = Point(1, 2)
    pointB = Point(3, 0)
    print(line2.point_line_distance(pointA))  # 2.5298221281347035
    line3 = Line.lineFromPoints(pointA, pointB)
    print(line3)  # Line 2x + 2y + -6 = 0
