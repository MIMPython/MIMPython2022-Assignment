print("Bài 4: Triangle Area")

from math import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dientich(self, dtB, dtC):
        t1 = (dtB.x - self.x)*(dtC.y - self.y)
        t2 = (dtC.x - self.x)*(dtB.y - self.y)
        s = (0.5)*abs(t1 - t2)
        print("Diện tích tam giác ABC là:", s)

print("Nhập tọa độ điểm A(xA, yA):")
xA = int(input("Nhập hoành độ điểm A với xA = "))
yA = int(input("Nhập tung độ điểm A với yA = "))
dtA = Point(xA, yA)
print("Nhập tọa độ điểm B(xB, yB):")
xB = int(input("Nhập hoành độ điểm B với xB = "))
yB = int(input("Nhập tung độ điểm B với yB = "))
dtB = Point(xB, yB)
print("Nhập tọa độ điểm C(xC, yC):")
xC = int(input("Nhập hoành độ điểm C với xC = "))
yC = int(input("Nhập tung độ điểm C với yC = "))
dtC = Point(xC, yC)
print()

#Diện tích tam giác ABC
dtA.dientich(dtB, dtC)
