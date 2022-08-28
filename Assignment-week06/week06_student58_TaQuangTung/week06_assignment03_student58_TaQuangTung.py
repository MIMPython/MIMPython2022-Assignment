print("Bài 3: Plotting Method")
import matplotlib.pyplot as plt
from sympy import *

class plottingMethod:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point(self):
        print(f"Tọa độ điểm là ({self.x}, {self.y})")
        plt.plot(self.x, self.y, "go")
        plt.title("BIỂU DIỄN TỌA ĐỘ ĐIỂM TRÊN MẶT PHẲNG OXY")
        plt.xlabel("Hoành độ x")
        plt.ylabel("Tung độ y")
        plt.show()
    def straightLine(self, plottingMethod):
        print(f"Tọa độ điểm đầu là ({self.x}, {self.y})")
        print(f"Tọa độ điểm sau là ({plottingMethod.x}, {plottingMethod.y})")
        plt.plot([self.x, plottingMethod.x], [self.y, plottingMethod.y], "go-")
        plt.title("BIỂU DIỄN ĐOẠN THẲNG TRÊN MẶT PHẲNG OXY")
        plt.xlabel("Hoành độ x")
        plt.ylabel("Tung độ y")
        plt.show()
    def circle(self, r):
        print(f"Hình tròn tâm I({self.x}, {self.y}) có bán kính r = {r}")
        x, y = symbols('x y')
        p = plot_implicit(Eq((x-self.x)**2 +(y-self.y)**2, r**2), (x, -r + self.x, r + self.x), (y, -r+ self.y, r+self.y), aspect_ratio = (1.,1.))

xA = float(input("Nhập hoành độ điểm A với xA = "))
yA = float(input("Nhập tung độ điểm A với yA = "))

#Tọa độ điểm A trên mặt phẳng Oxy
pointA = plottingMethod(xA, yA)
pointA.point()    
print()      


#Đoạn thẳng BC trên mặt phẳng Oxy
xB = float(input("Nhập hoành độ điểm B với xB = "))
yB = float(input("Nhập tung độ điểm B với yB = "))
pointB = plottingMethod(xB, yB)
xC = float(input("Nhập hoành độ điểm C với xC = "))
yC = float(input("Nhập tung độ điểm C với yC = "))
pointC = plottingMethod(xC, yC)
pointB.straightLine(pointC)
print()


#Đường tròn trong mặt phẳng Oxy
xI = float(input("Nhập hoành độ tâm I với xI = "))
yI = float(input("Nhập tung độ tâm I với yI = "))
r = float(input("Nhập bán kính r = "))
pointI = plottingMethod(xI, yI)
pointI.circle(r)
