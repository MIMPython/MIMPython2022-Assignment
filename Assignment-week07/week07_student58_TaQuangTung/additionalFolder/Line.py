# Khởi tạo đối tượng đường thẳng 

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
    def Lining(self):
        print(f"Phương trình đường thẳng là: {self.a}*x + {self.b}*y + c = 0")

print("ĐƯỜNG THẲNG")
a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))
c = float(input("Nhập hệ số c = "))

Line(a, b, c).Lining()
print()