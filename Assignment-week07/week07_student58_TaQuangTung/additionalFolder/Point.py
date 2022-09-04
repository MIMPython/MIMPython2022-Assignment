# Khởi tạo đối tượng điểm

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def pointing(self):
        print("Hoành độ điểm x =", self.x)
        print("Hoành độ điểm y =", self.y)
        print("Tọa độ điểm là:", (self.x, self.y))

print("ĐIỂM")
x = float(input("Nhập hoành độ điểm: "))
y = float(input("Nhập tung độ điểm: "))
Point(x, y).pointing()
print()
