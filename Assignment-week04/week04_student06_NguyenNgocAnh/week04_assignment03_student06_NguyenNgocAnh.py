import math

from week04_assignment02_student06_NguyenNgocAnh import Point

"""
Bài tập 3. (class Line)
Xây dựng class Line để biểu diễn các đường thẳng trong mặt
phẳng Oxy dựa theo những câu hỏi/yêu cầu dưới đây.

(a) Vì sao phương trình đường thẳng có dạng y=ax+b với a,b là hai
tham số bất kỳ không phải là phương trình tổng quát của một đường
thẳng trong mặt phẳng Oxy? Đường thẳng nào không biểu diễn được
qua phương trình này?

(b) Xét phương trình ax+by+c=0 với a,b,c là ba tham số bất kỳ.
Tìm điều kiện của ba tham số a,b,c để phương trình này là phương
trình tổng quát của một đường thẳng trong mặt phẳng Oxy.

(c) Phần khởi tạo của class Line có thể được viết như sau

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
Nhận xét đoạn code trên.

(d) Viết một phương thức trong class Line để xác định
(những) giao điểm của hai đường thẳng (nếu có), đồng
thời tự quyết định kiểu dữ liệu trả về của phương thức này.

Bình luận

Về mặt toán học, có tất cả ba trường hợp có thể xảy ra khi
xét đến giao điểm của hai đường thẳng:
Trường hợp 1: hai đường thẳng không có giao điểm
Trường hợp 2: hai đường thẳng có duy nhất một giao điểm
Trường hợp 3: hai đường thẳng trùng nhau, có vô số giao điểm
Với ba trường hợp có thể xảy ra kể trên, có hai cách thiết kế dữ liệu trả về của phương thức này:

Cách cơ bản

Trường hợp 1: trả về một tuple rỗng
Trường hợp 2: trả về một tuple có một phần tử là một
giao điểm với kiểu dữ liệu Point
Trường hợp 3: trả về một giá trị phù hợp nào đó
Cách nâng cao (liên quan đến cấu trúc try-except)

Trường hợp 1: raise ValueError('no roots')
Trường hợp 2: trả về một giao điểm với kiểu dữ liệu Point
Trường hợp 3: raise ValueError('infinite roots')
(e) Viết một method trong class Line để xác định khoảng cách giữa một điểm và một đường thẳng.

(f) Biết rằng có duy nhất một đường thẳng đi qua hai điểm phân
biệt cho trước. Viết một method trong class Line để khởi tạo một
đường thẳng (là một instance của class Line) với tham số đầu vào
là hai instance của class Point. Gợi ý: Sử dụng @classmethod
"""

"""
(a) y = ax + b không thể hiện toàn bộ đường thẳng được biểu diễn
vd như x = 0 
"""


class Line:
    def __init__(self, a, b, c):
        if a == 0 and b == 0:
            print('Nhập lại!')
        self.a = a
        self.b = b
        self.c = c
        # đoạn code trên sẽ gây sai ở trường hợp
        # a = 0, b = 0, c # 0 hoặc c = 0

    def distance_point_to_line(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    @classmethod
    def find_line(cls, point1, point2):
        if point1 != point2:

            if point2.y != point1.y:
                a = 1
                b = (point1.x - point2.x) / (point2.y - point1.y)
                c = -a * point1.x - b * point1.y

            else:
                a = 0
                b = 1
                c = -point1.y
            return Line(a, b, c)

        else:
            return False


if __name__ == '__main__':
    l1 = Line(-2, 2, 3)
    l2 = Line(-4, 3, 6)
    A = Point(1, 0)
    print(Line.find_line(A, Point(0, 0)))
    print(l1.distance_point_to_line(A))
