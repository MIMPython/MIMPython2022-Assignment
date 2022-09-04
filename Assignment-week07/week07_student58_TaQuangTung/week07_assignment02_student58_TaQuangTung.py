print("Bài 2: Class Inheritance")

from math import *
from turtle import circle

# Đối tượng ban đầu là HCN
class Rectangle:
    def __init__(self, a, b):
        self.a = a      # Chiều dài
        self.b = b      # Chiều rộng 
    def chuVi(self):
        print("Chu vi của HCN là:", 2*(self.a + self.b))
    def dienTich(self):
        print("Diện tích của HCN là:", self.a * self.b)

# Nhập dữ liệu đầu vào
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
Rectangle(a, b).chuVi()
Rectangle(a, b).dienTich()
print()

# Đối tượng Hình Vuông
class Square(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, b)     #Kế thừa độ dài cạnh của Rectangle
    def chuViHV(self):
        print("Chu vi hình Vuông là:", 4*self.a)
    def dienTichHV(self):
        print("Diện tích hình Vuông là:", self.a**2)
Square(a, b).chuViHV()
Square(a, b).dienTichHV()
print()

# Đối tượng Hình Thoi
class Rhombus(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, b)      
        # Khi đó sẽ kế thừa độ dài hai cạnh của HCN thành độ dài hai đường chéo của hình thoi
    def chuViHT(self):
        d = sqrt((self.a/2)*2 + (self.b/2)**2)
        print("Chu vi Hình Thoi là:", 4*d)
    def dienTichHT(self):
        print("Diện tích Hình Thoi là:", self.a*self.b/2)
Rhombus(a, b).chuViHT()
Rhombus(a, b).dienTichHT()
print()


# Khởi tạo đối tượng Ellipse
class Ellipse:
    def __init__(self, r1, r2):
        self.r1 = r1        # Bán kính trục lớn
        self.r2 = r2        # Bán kính trục bé
    def ChuViE(self):
        P = 2*pi*sqrt((self.r1**2 + self.r2**2)/2)
        return P
    def DienTichE(self):
        S = pi*self.r1*self.r2 
        return S
r1 = float(input("Độ dài nửa trục lớn là: "))
r2 = float(input("Độ dài nửa trục bé là: "))
elip = Ellipse(r1, r2)
print("Chu vi Hình Elipse là:", elip.ChuViE())
print("Diện tích Hình Eclipse là:", elip.DienTichE())
print()

# Kế thừa cho đối tượng Hình Tròn
class Circle(Ellipse):
    def __init__(self, r1, r2):
        super().__init__(r1, r2)
    def ChuViE(self):
        return super().ChuViE()
    def DienTichE(self):
        return super().DienTichE()
r = float(input("Nhập bán kính hình tròn: "))
circle = Circle(r, r)
print("Chu vi Hình Tròn là:", circle.ChuViE())
print("Diện tích Hình Tròn là:", circle.DienTichE())
