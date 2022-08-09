print("Bài 6: Class Circle")

from sympy import *
from math import sqrt 

class Circle:
    def __init__(self, x0, y0, r):
        self.x0 = x0
        self.y0 = y0
        self.r = r
    def kiemtra(self):
        # (x - x0)**2 + (y - y0)**2 = r**2
        # y1 = y0 + sqrt(r**2 - (x - x0)**2)
        # y2 = y0 - sqrt(r**2 - (x - x0)**2)
        x, y = symbols('x y')
        p = plot_implicit(Eq((x-self.x0)**2 +(y-self.y0)**2, r**2), (x, -r + self.x0, r+ self.x0), (y, -r+ self.y0, r+self.x0), aspect_ratio = (1.,1.))


x0 = float(input("Nhập hoành độ tâm: "))
y0 = float(input("Nhập tung độ tâm: "))
r = float(input("Nhấp bán kính hình tròn: "))
diem = Circle(x0, y0, r)
diem.kiemtra()