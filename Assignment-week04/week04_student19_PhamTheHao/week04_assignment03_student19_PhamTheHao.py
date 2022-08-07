"""
Bài tập 3. (class Line)
Xây dựng class Line để biểu diễn các đường thẳng trong mặt phẳng Oxy dựa theo những 
câu hỏi/yêu cầu dưới đây.
(a) Vì sao phương trình đường thẳng có dạng y=ax+b với a,b là hai tham số bất kỳ không 
phải là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy? Đường thẳng nào 
không biểu diễn được qua phương trình này?
(b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ. Tìm điều kiện của ba 
tham số a,b,c để phương trình này là phương trình tổng quát của một đường thẳng trong 
mặt phẳng Oxy.
(c) Phần khởi tạo của class Line có thể được viết như sau. Nhận xét đoạn code trên.
(d) Viết một phương thức trong class Line để xác định (những) giao điểm của hai đường 
thẳng (nếu có), đồng thời tự quyết định kiểu dữ liệu trả về của phương thức này.
(e) Viết một method trong class Line để xác định khoảng cách giữa một điểm và một đường 
thẳng.
(f) Biết rằng có duy nhất một đường thẳng đi qua hai điểm phân biệt cho trước. Viết một 
method trong class Line để khởi tạo một đường thẳng (là một instance của class Line) với 
tham số đầu vào là hai instance của class Point. Gợi ý: Sử dụng @classmethod
"""

# a) Vì nó không biểu diễn hết được tất cả các đường thằng. Ví dụ đường thẳng x = 0
# b) Nếu a = 0 và b = 0: PT đã cho không phải pt đường thẳng. Vậy ít nhất 1 trong 2 số
#    a và b phải khác 0.

import math

def determinant(line_1, line_2):
        return line_1.a * line_2.b - line_1.b * line_2.a

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
#d)
    def intersection_of_two_line(line_1, line_2):
        if determinant(line_1, line_2) == 0:
            if line_1.a == line_2.a:
                return 'Two lines are duplicate'
            else:
                return ()
        else:
            x = (line_1.c * line_2.b - line_2.c * line_1.b) / determinant(line_1, line_2)
            y = (line_1.a * line_2.c - line_2.a * line_1.c) / determinant(line_1, line_2)
            return (Point(x, y),)
#e)
    def distance_point_line(point, line):
        return abs(line.a * point.x + line.b * point.y + line.c) / math.sqrt(line.a ** 2 + line.b ** 2)

#f)
    @classmethod
    def line_through_two_point(A, B):
        a = B.y - A.y

        if A.x - B.y < 0:
            b = B.x - A.x
        else:
            b = A.x - B.x

        c = a * A.x + b * A.y

        return Line(a, b, c)

if __name__ == '__main__':
    

    Line1 = Line(1, 3, 1)
    Line2 = Line(2, 1, 0)

    Line3 = Line(1, 3, 1)
    Line4 = Line(1, 3, 1)

    PointA = Point(1, 3)
    PointB = Point(3, 1)

    print(Line.intersection_of_two_line(Line1, Line2))  #(-0.2, 0.4)
    print(Line.distance_point_line(PointA, Line1))      # 3.478505426185217
    print(Line.line_through_two_point(PointA, PointB))



 

