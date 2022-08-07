"""
a. phương trình đường thẳng dạng y = ax + b
    đường thẳng qua hai điểm bất kì có phương trình y = ax + b có nghĩa là
    hệ phương trình: ax + b = y và ax' + b = y' có nghiệm ( với 2 ẩn là a, b)
    hay ma trận tương ứng có định thức khác 0 được tính như sau: |x - x'| >< 0
    như vậy trường hợp x = x' phương trình trên vô nghiệm.
    mặt khác tồn tại đường thẳng có 2 điểm sao cho tọa độ điểm x tương ứng của chúng bằng nhau
    vậy những đường thẳng dạng x = k sẽ không biểu diễn được với phương trình dạng y = ax + b

b. ax + by + c = 0 phương trình có vô số nghiệm trong nhiều trường hợp
    để phương trình là một phương trình đường thẳng thì không gian nghiệm của phương trình là
    không gian 1 chiều
    Ta xét các không gian nghiệm có thể có của phương trình trên:
    với a != 0 và b != 0
        KG no: y = (-ax -c)/b, x thuộc R --> vector cơ sở: (1, (-a -c)/b) --> KG 1 chiều
    với a != 0 và b == 0
        KG no: x = -c/a, y thuộc R --> vector cơ sở: (-c/a, 1) --> KG 1 chiều
    với a == 0 và b != 0
        KG no: y = -c/b, x thuộc R --> vector cơ sở: (-c/b, 1) --> KG 1 chiều
    với a == 0 và b == 0 không thể tìm được không gian nghiệm khi c != 0, khi c == 0:
        KG no: x thuộc R, y thuộc R --> vector cở sở: (1,0) (0,1) --> KG 2 chiều
    Vậy phương trình là phương trình đường thẳng khi a và b khác 0 hay a^2 + b^2 != 0

c. Đoạn code trên tạo đường thẳng một cách tự do chưa check đến điều kiện tồn tại đường thẳng
    ở câu b
"""
import itertools
import math
from math import sqrt

from week04_assignment02_student33_HoangNhatMinh import Point


class Line:
    def __init__(self, a, b, c):
        if a ** 2 + b ** 2 != 0:
            # rút gọn trước khi gán giá trị
            listValue = [abs(a), abs(b), abs(c)]
            GCD = tmp if (tmp := math.gcd(*listValue)) != 0 else 1
            self.a = a / GCD
            self.b = b / GCD
            self.c = c / GCD
        else:
            raise ValueError(f'Invalid value, "{a}x + {b}y + {c} = 0" is not a line')

    def intersectionPoint(self, *args):
        if self.a == args[0] and self.b == args[1]:
            if self.c == args[2]:
                raise ValueError('infinite roots')
            else:
                raise ValueError('no roots')
        else:
            # sử dụng quy tắc Cramer để giải
            D = self.a * args[1] - self.b * args[0]
            Dx = self.c * args[1] - self.b * (-args[2])
            Dy = self.a * (-args[2]) - self.c * args[0]
            return Dx / D, Dy / D

    def distanceTo(self, *args: Point) -> float:
        if len(args) == 2:
            return abs(self.a * args[0] + self.b * args[1] + self.c) / sqrt(self.a ** 2 + self.b ** 2)
        elif len(args) == 3:
            x = 0
            y = -args[2]/args[1]
            self.distanceTo(x, y)

    @classmethod
    def constructor(cls, p1: Point, p2: Point):
        directionVector = (-p1.y + p2.y, p1.x - p2.x)
        c = - directionVector[0] * p1.x - directionVector[1] * p1.y
        return Line(directionVector[0], directionVector[1], c)

    def __repr__(self):
        listValue = []
        for v in self.__dict__.values():
            if v > 0:
                listValue.append(' + ' + str(v) if len(listValue) != 0 else str(v))
            elif v < 0:
                listValue.append(' - ' + str(abs(v)))
            else:
                listValue.append('')
        return listValue[0] + 'x' + listValue[1] + 'y' + listValue[2] + ' = 0'


if __name__ == '__main__':
    l1 = Line(1, -1, 0)
    l2 = Line(-2, -2, 4)
    print(l2)  # - 1.0x - 1.0y + 2.0 = 0
    print(l1.intersectionPoint(*l2.__dict__.values()))  # (1.0, 1.0)
    print(l2.distanceTo(*Point(0, 0).__dict__.values()))  # 1.414213562373095 = sqrt(2)/2
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    l3 = Line.constructor(p2, p1)
    print(l3)  # - 1.0x - 1.0y = 0
