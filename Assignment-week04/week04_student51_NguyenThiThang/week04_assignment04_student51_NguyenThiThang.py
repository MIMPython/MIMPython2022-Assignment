
from telnetlib import X3PAD
from tkinter import SEL_LAST
from tokenize import Double
from zlib import DEFLATED


class triangleArea:
    def __init__(self,x1,x2,x3,y1,y2,y3):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.y1=y1
        self.y2=y2
        self.y3=y3

    def dienTich(self):
        S=self.x1*(self.y2-self.y3)+self.x2*(self.y3-self.y1)+self.x3*(self.y1-self.y2)/2
        if S==0:
            print("Cac diem da cho khong tao thanh tam giac")
        else:
            return S

if __name__=='__main__':
    x1=float(input("Nhap hoanh do diem thu nhat "))
    y1=float(input("Nhap tung do diem thu nhat "))
    x2=float(input("Nhap hoanh do diem thu hai "))
    y2=float(input("Nhap tung do diem thu hai "))
    x3=float(input("Nhap hoanh do diem thu ba "))
    y3=float(input("Nhap tung do diem thu ba "))
    print("Dien tich tam giac tren la:")
    s=triangleArea(x1,x2,x3,y1,y2,y3).dienTich()
    print(s)

         