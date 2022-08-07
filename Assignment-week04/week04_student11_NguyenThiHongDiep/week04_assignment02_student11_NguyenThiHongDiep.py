import math
class Point:
# 1. Thiết kế phần khởi tạo của class Point (chọn tên thuộc tính phù hợp) và khởi tạo một số instance của class này.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    pointA = Point(2, -3)
    pointB = Point(3, 8)
    pointC = Point(-2, -6)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
# 2. Viết hàm distance() thuộc class Point để tính khoảng cách Euclid (hay còn gọi là chuẩn L2) giữa hai instance của class Point.
    def distance(A, B):
        xA = A.getX
        yA = A.getY
        xB = B.getX
        yB = B.getY
        dis = math.sqrt((xA - xB)**2 + (yA - yB)**2)
        return(dis)

    print(distance(pointA, pointB))

# 3. Bổ sung tham số metric (nhận giá trị là một str) trong hàm distance() vừa viết để tính khoảng cách giữa hai điểm theo một trong hai metric: khoảng cách Euclid (chuẩn L2) hoặc khoảng cách Manhattan (chuẩn L1). Dưới đây là ví dụ cách sử dụng hàm


