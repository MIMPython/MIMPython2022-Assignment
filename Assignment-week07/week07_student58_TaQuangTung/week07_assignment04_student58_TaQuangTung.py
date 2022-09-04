from math import gcd
print("Bài 4: Class Fraction")

class Fraction:
    def __init__(self, ts, ms):
        self.ts = ts
        self.ms = ms
    def __str__(self):
        return "({0}, {1})".format(self.ts, self.ms)
    
    @classmethod
    def initializeFromFloat(self, thapphan):
        thap = str(thapphan).split(".")
        if thap[0] == '0':
            tu = int(thap[1])
            mau = int(thap[0]) + 10**(len(thap[1]))
            d = gcd(tu, mau)        # Ước chung lớn nhất
            tu //= d
            mau //= d
            return Fraction(tu, mau)
        else:
            tu = int(thap[0] + thap[1])
            mau = 10**(len(thap[1]))
            d = gcd(tu, mau)
            tu //= d
            mau //= d
            return Fraction(tu, mau)
        

    # Nạp chồng toán tử so sánh
    def __lt__(self, other):
        return (self.ts/self.ms) < (other.ts/other.ms)
    def __le__(self, other):
        return (self.ts/self.ms) <= (other.ts/other.ms)
    def __eq__(self, other):
        return (self.ts/self.ms) == (other.ts/other.ms)
    def __ne__(self, other):
        return (self.ts/self.ms) != (other.ts/other.ms)
    def __gt__(self, other):
        return (self.ts/self.ms) > (other.ts/other.ms)
    def __ge__(self, other):
        return (self.ts/self.ms) >= (other.ts/other.ms)

    # Tính tổng ba đối tượng
    def __add__(self, other1, other2):
        return self.ts/self.ms + other1.ts/other1.ms + other2.ts/other2.ms

# foo = Fraction(2, 3)
# bar = Fraction.initializeFromFloat(0.42)
ts = int(input("Nhập tử số: "))
ms = int(input("Nhập mẫu số: "))
foo = Fraction(ts, ms)
thapphan = float(input("Nhập số thập phân: "))
print(thapphan)
bar = Fraction.initializeFromFloat(thapphan)
print(foo)
print(bar)
print()

print("SO SÁNH GIỮA CÁC ĐỐI TƯỢNG")
print(f"foo < bar => {foo < bar}")
print(f"foo <= bar => {foo <= bar}")
print(f"foo == bar => {foo == bar}")
print(f"foo != bar => {foo != bar}")
print(f"foo > bar => {foo > bar}")
print(f"foo >= bar => {foo >= bar}")
print()

print("NHẬN XÉT")
fr1 = Fraction(2, 3)
fr2 = Fraction(1, 3)
fr3 = Fraction(3, 5)
totalValue = Fraction.__add__(fr1, fr2, fr3)
print(totalValue)

"""
Kết luận: 
+ Theo em thì sau khi sử dụng __add__ thì không thể sử dụng cách viết:
    totalValue = sum([fractionA, fractionB, fractionC])
Bởi vì: 
+ Bản chất __add__ đã là tính tổng của các đối tượng trong khi đó sum([mảng]) là thực hiện tính tổng theo các phần tử trong mảng
+ Hai phương thức tính tổng trên là khác nhau
=> Nên không thể ép đối tượng thành phần tử trong mảng
"""
