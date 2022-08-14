'''
Xây dựng class Point để biểu diễn các điểm trong mặt phẳng tọa độ Oxy.
'''
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
# 2. Tính khoảng cách Euclid (hay còn gọi là chuẩn L2) giữa hai instance của class Point.
# 3. Bổ sung tham số metric (nhận giá trị là một str) trong hàm distance() vừa viết để tính khoảng cách giữa hai điểm theo một trong hai metric: khoảng cách Euclid (chuẩn L2) hoặc khoảng cách Manhattan (chuẩn L1).
    def distance(self, other, metric):
        distanceL2 = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        distanceL1 = abs(self.x - other.x) + abs(self.y - other.y)
        
        if metric == "L1":
            return distanceL1
        if metric == "L2":
            return distanceL2
    
# 4. Viết một method để tạo một điểm đối xứng với một điểm cho trước qua gốc tọa độ. 
# Cách 2. Viết một hàm thuộc class Point để có thể sử dụng hàm bằng cách viết (ví dụ như) pointA.getSomething().
    def getSymmetryPoint(self):
        return -(self.x), -(self.y)

# 5. Bổ sung hàm __repr__() cho class Point.
    def __repr__(self):
        return f'({self.x},{self.y})'


pointA = Point(2,-3)
pointB = Point(11,8)

print(pointA.distance(pointB, metric = 'L2')) #10.295630140987
print(pointA.distance(pointB, metric = 'L1')) #14
print(pointA.getSymmetryPoint()) #(-2, 3)
print(repr(pointA)) #(2,-3)