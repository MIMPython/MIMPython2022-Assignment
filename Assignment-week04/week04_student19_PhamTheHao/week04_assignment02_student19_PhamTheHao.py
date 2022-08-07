"""
Bài tập 2. (class Point)
Xây dựng class Point để biểu diễn các điểm trong mặt phẳng tọa độ Oxy.
1. Thiết kế phần khởi tạo của class Point (chọn tên thuộc tính phù hợp) và khởi tạo 
    một số instance của class này.
2. Viết hàm distance() thuộc class Point để tính khoảng cách Euclid (hay còn gọi là 
    chuẩn L2) giữa hai instance của class Point.
3. Bổ sung tham số metric (nhận giá trị là một str) trong hàm distance() vừa viết để 
    tính khoảng cách giữa hai điểm theo một trong hai metric: khoảng cách Euclid 
    (chuẩn L2) hoặc khoảng cách Manhattan (chuẩn L1).
4. Viết một method để tạo một điểm đối xứng với một điểm cho trước qua gốc tọa độ. 
    Thực hiện yêu cầu này bằng một trong ba cách dưới đây:
    Cách 1. Viết một hàm tách biệt so với class Point, nhận vào một instance của class 
    Point và trả về một instance mới.
    Cách 2. Viết một hàm thuộc class Point để có thể sử dụng hàm bằng cách viết (ví dụ 
    như) pointA.getSomething().
    Cách 3. Cũng thực hiện như cách 2, nhưng trong nội dung của hàm này không có chữ 
    Point. Gợi ý: sử dụng thuộc tính self.__class__.
5. Bổ sung hàm __repr__() cho class Point.
"""

from turtle import distance


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def distance(A, B, metric):
        if metric == 'L2':
            return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5
        elif metric == 'L1':
            return abs(A.x - B.x) + abs(A.y - B.y)

    def symmetric_point(A):
        print('({}, {})'.format(- A.x, - A.y))

if __name__ == '__main__':
    
    PointA = Point(1, 3)
    PointB = Point(2, 1)

    print(Point.distance(PointA, PointB, 'L2'))   # 2.23606797749979
    Point.symmetric_point(PointA)                 # (-1, -3)
    print(Point.__repr__(PointB))                 # (2, 1)





