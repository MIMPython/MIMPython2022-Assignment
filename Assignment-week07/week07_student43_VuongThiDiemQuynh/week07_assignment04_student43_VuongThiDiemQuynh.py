'''
Bài tập 4. (class Fraction)
Thiết kế class Fraction với hai thuộc tính cơ bản gồm tử số và mẫu số (có thể thay đổi thuộc tính nếu cần thiết). Ngoài ra, xây dựng thêm những phương thức phù hợp để mô phỏng cách sử dụng một phân số trong những công việc thực tế. Dưới đây là một ví dụ minh họa

foo = Fraction(2,3)
bar = Fraction.initializeFromFloat(0.42)
print(bar) # Frac(21,50)
print(foo >= bar) # True

Câu hỏi nâng cao. Sau khi đã cài đặt __add__, liệu có thể sử dụng cách viết
totalValue = sum([fractionA, fractionB, fractionC])
được hay không?
'''
import math 
import fractions 

class Fraction:
    def __init__(self, numerator, denominator):
        GCD = math.gcd(numerator, denominator)
        self.top = int(numerator / GCD)
        self.bottom = int(denominator / GCD)
        # Neu khong ep kieu thanh int: TypeError: both arguments should be Rational instances
    
    @classmethod
    def __str__(self):
        if self.bottom == 1:
            return f"{self.top}"    
        else:
            return f"{self.top}/{self.bottom}"

    def initializeFromFloat(float):
        return fractions.Fraction(float).limit_denominator()

    def __add__(self, other):
            return fractions.Fraction(self.top * other.bottom + other.top * self.bottom, self.bottom * other.bottom)
    
if __name__ == '__main__':
    fractionA = Fraction(1, 2)
    fractionB = Fraction(3, 9)
    fractionC = Fraction.initializeFromFloat(0.42)
    sumAB = fractionA + fractionB 
    print(sumAB) # 5/6
    print(fractionC) # 21/50
