print("Bài 3: Class Line")
print()

from random import *
from math import *
"""
a) Phương trình đường thẳng y = ax+b với a, b bất kỳ không là phương trình tổng quát trong Oxy
Ta có phương trình đường thẳng ax - y + b = 0 luôn có vtpt là (a,-1) 
Bởi khi đó tồn tại 1 số phương trình đường thẳng không có sự phụ thuộc giữa hai biến x và y
VD: y = c hay x = d với c, d là hằng số bất kỳ

b) Xét phương trình ax+by+c=0 với a,b,c bất kỳ. Điều kiện phương trình này là phương trình tổng quát trong Oxy
+ Nếu a = 0, b = 0, c = 0: Hàm hằng c = 0
+ Nếu a = 0, b = 0, c != 0: Không tồn tại PTTQ
+ Nếu a = 0, b != 0: y = -c/b
+ Nếu a != 0, b = 0: x = -c/a
+ Nếu a != 0, b != 0: ax + by + c = 0

c) Nhận xét đoạn code
+ Ngay sau khi gọi đối tượng thì thực hiện phương thức khởi tạo đầu tiên __init__()
+ Khai báo thuộc tính đối tượng 
+ Hàm khởi tạo được sử dụng để gán giá trị cho các thuộc tính của đối tượng hoặc thực hiện một số thao tác khi đối tượng đang được tạo ra
"""
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def tuonggiao(self, Line):
        tup = ()
        # a1*x + b1*y + c1 = 0 => a1*x + b1*y = -c1
        # a2*x + b2*y + c2 = 0 => a2*x + b2*y = -c2
        
        # Cho pt1 - pt2: (a1 - a2)*x + (b1 - b2)*y = -c1 + c2
        # (b1 - b2)* y = (a2 - a1)*x + (c2 - c1)
        if self.b - Line.b == 0:
            # (a2 - a1)*x = (c1 - c2)
            if Line.a - self.a == 0:
                # 0*x = (c1 - c2)
                if self.c - Line.c == 0:
                    print("Có vô số hoành độ giao điểm")
                    x = randint(1,10)
                else:
                    print("Không tồn tại hoành độ giao điểm")
                    x = " "
            else:
                x = (self.c - Line.c)/(Line.a - self.a)
                print("Hoành độ giao điểm x =", x)
        else:
            # y = x*(a2 - a1)/(b1 - b2) + (c2 - c1)/(b1 - b2)
            # Thay vào pt1:
            """
            (a1 - b1*(a1-a2)/(b1-b2))*x = b1*(c1-c2)/(b1-b2) - c1
            """
            hsa = self.a - self.b*(self.a-Line.a)/(self.b-Line.b)
            hsc = self.b*(self.c-Line.c)/(self.b-Line.b) - self.c
            if hsa == 0:
                if hsc == 0:
                    print("Có vô số hoành độ giao điểm")
                    x = randint(1,10)
                else:
                    print("Không tồn tại hoành độ giao điểm")
                    x = " "
            else:
                x = hsc/hsa
                print("Hoành độ giao điểm x =", x)
        tup += (x, )

        # Thay lại x vào pt1 hoặc pt2
        # b1*y = -a1*x - c1
        if self.b == 0:
            try:
                if -self.a * x - self.c == 0:
                    print("Có vô số tung độ giao điểm")
                    y = randint(1,10)
                else:
                    print("Không tồn tại tung độ giao điểm")
                    y = " "
            except:
                print("Không tồn tại tọa độ giao điểm")
        else:
            y = (-self.a * x - self.c)/self.b 
            print("Tung độ giao điểm y =", y)
        
        tup += (y, )
        print("Tọa độ giao điểm của hai đường thẳng là:",tup)

    
    def khoangcach(self):
        hoanhdo = float(input("Nhập hoành độ x = "))
        tungdo = float(input("Nhập tung độ y = "))

        ts = abs((self.a)*hoanhdo + (self.b)*tungdo + self.c)
        ms = sqrt((self.a)**2 + (self.b)**2)
        print(f"Khoảng cách từ điểm ({hoanhdo}, {tungdo}) đến đường thẳng là:", ts/ms)

    @classmethod
    def duongthang(cls, xA, yA, xB, yB):
        vtcp_x = xB - xA
        vtcp_y = yB - yA 

        vtpt_x = -vtcp_y
        vtpt_y = vtcp_x
        # vtpt_x *(x - xA) + vtpt_y *(y - yA) = 0
        print(f"Phương trình đường thẳng AB là: ({vtpt_x})*X + ({vtpt_y})*Y {-xA*vtpt_x - yA*vtpt_y} = 0")
print("Phương trình đường thẳng d1: ")
a1 = float(input("Nhập hệ số a1 của d1: "))
b1 = float(input("Nhập hệ số b1 của d1: "))
c1 = float(input("Nhập hệ số c1 của d1: "))
dtA = Line(a1, b1, c1)
print("Phương trình đường thẳng d2: ")
a2 = float(input("Nhập hệ số a1 của d2: "))
b2 = float(input("Nhập hệ số b1 của d2: "))
c2 = float(input("Nhập hệ số c1 của d2: "))
dtB = Line(a2, b2, c2)
print()

dtA.tuonggiao(dtB)      #Độ tương giao hai đường thẳng
print()

#Khoảng cách từ 1 điểm tới đường thẳng
dtA.khoangcach()        #Khoảng cách từ đến dtA
print()
dtB.khoangcach()        #Khoảng cách từ đến dtB
print()

#Tạo đường thẳng từ hai điểm đã cho
xA = float(input("Nhập hoành độ điểm A với xA = "))
yA = float(input("Nhập tung độ điểm A với yA = "))
xB = float(input("Nhập hoành độ điểm A với xB = "))
yB = float(input("Nhập tung độ điểm A với yB = "))
Line.duongthang(xA, yA, xB, yB)
