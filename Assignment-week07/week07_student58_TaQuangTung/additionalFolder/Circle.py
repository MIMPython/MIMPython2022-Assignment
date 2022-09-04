# Khởi tạo đối tượng hình tròn

class Circle:
    def __init__(self, x0, y0, r):
        self.x0 = x0
        self.y0 = y0 
        self.r = r 
    def Circling(self):
        print(f"Hình tròn là: (x - {self.x0})^2 + (y - {self.y0})^2 = {self.r**2}")

print("HÌNH TRÒN")
x0 = float(input("Nhập hoành độ tâm x0 = "))
y0 = float(input("Nhập tung độ tâm y0 = "))
r = float(input("Nhập bán kính r = "))
Circle(x0, y0, r).Circling()
print()