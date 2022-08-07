print("Bài 2: Class Point")
print()

from math import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, Point, metric):
        # L2 = sqrt((xA-xB)**2 + (yA-yB)**2)
        # L1 = abs(xA-xB) + abs(yA-yB)
        
        L2 = sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        L1 = abs(self.x - Point.x) + abs(self.y - Point.y)
        
        if metric == 'L1':
            print("Khoảng cách theo Manhattan:",L1)
        if metric == 'L2':
            print("Khoảng cách theo Euclid:",L2)

    def getSomething(self):
        xp = -self.x
        yp = -self.y
        print(f"Điểm ({self.x}, {self.y}) đối xứng qua gốc tọa độ là:", (xp, yp))

    def __repr__(self):
        return repr(f'Tọa độ điểm là ({self.x}, {self.y})')
        

print("Nhập tọa độ điểm A")
xA = float(input("Nhập xA = "))
yA = float(input("Nhập yA = "))
pointA = Point(xA, yA)
print("Nhập tọa độ điểm B")
xB = float(input("Nhập xB = "))
yB = float(input("Nhập yB = "))
pointB = Point(xB, yB)

metric = input("Nhập không gian metric: ")      #Chỉ chọn L1 hoặc L2
pointA.distance(pointB, metric)     #Khoảng cách Euclid và Manhattan
print() 

#Tọa độ điểm đối xứng qua tâm O(0,0)
pointA.getSomething()
pointB.getSomething()
print()

#Sử dụng hàm Point
print(repr(pointA))
print(repr(pointB))
