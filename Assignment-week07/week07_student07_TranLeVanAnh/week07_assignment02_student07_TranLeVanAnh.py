#Bài 2
#1
from turtle import width
from math import pi

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("S = ", self.length*self.width)
rectangle1 = rectangle (length = 2, width = 3)
rectangle1.area()

class square(rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return super().area()
square1 = square(length=2,width=2)
square1.area()
#1'
class rhombus(rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area1(self):
        print("S = ", (self.length*self.width)/2)
rhombus1 = rhombus(length=2,width=3)
rhombus1.area1()
#2
class elip: 
    def __init__(self, r1, r2): #r1,r2 lần lượt là độ dài trục lớn và trục nhỏ
        self.r1 = r1
        self.r2 = r2
    def cir(self):
        print("P = ", 2*pi*(((self.r1)**2+(self.r2)**2)/2)**(1/2))
elip1 = elip(r1 = 4, r2 = 6)
elip1.cir()

class circle(elip):
    def __init__(self, r1, r2):
        super().__init__(r1, r2)
    def cir(self):
        return super().cir()
circle1 = circle(r1=2,r2=2)
circle1.cir()