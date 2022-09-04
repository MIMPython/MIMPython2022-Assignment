"""
Chương trình cho phép người dùng khởi tạo theo 2 kiểu
+ Nhập vào 1 số thực và sẽ trả về dạng số thập phân tối giản 
+ Nhập vào tử số và mẫu số cho và trả về dạng số tập phân tối giản kèm theo giá trị thực
(Ví dụ trong hàm main)
"""

class Fraction:
    __value__: float = 1.0
    __numerator__: int = 1
    __denominator__: int = 1

    """Phương thức này để khi người dùng nhập tử hoặc mẫu số là số không phải số nguyên sẽ đưa về
    dạng số nguyên với giá trị tương ứng
    Ví dụ người dùng nhập (a = 2.5 và b = 1 thì sau khi kết thúc sẽ trả về a = 25 b = 10)
     """

    @staticmethod
    def __int(a: float = ...,b: float = ...) -> tuple:
        while a % 1 != 0 or b % 1 != 0:
            b *= 10
            a *= 10
        return int(a), int(b)


    #Tìm ước chung lớn nhất để rút gọn phân số
    @staticmethod
    def __gcd(a: float, b: float) -> float:
        a, b = abs(a), abs(b)

        while a!=b:
            if a < 1 or b < 1:
                return 1
            if a < b: b-=a
            else: a -= b
        return a

    def __init__(self, a: float = ..., b: float = 1) -> None:
        self.setValue(a, b)

    def __repr__(self) -> str:
        a = self.__numerator__
        b = self.__denominator__

        if b < 0:
            a *= -1
            b = abs(b)

        if a == 0:
            return "0"
        if b == 1:
            return str(a)
        return "{} / {} = {}".format(a, b, self.__value__)

    def getValue(self):
        return self.__value__
    
    def setValue(self, a: float = ..., b: float = 1):
        a, b = self.__int(a, b)
        self.__value__ = a / b
        div = self.__gcd(a, b)
        self.__numerator__ = int(a / div)
        self.__denominator__ = int(b / div)


    """ Các phương thức dưới đây cho phép người dùng tính toán và so sánh phần số
    hay cho phép thực hiện các công việc của 1 đối tượng Fraction tương tự 1 phân số
    """
    def __add__(self, other) -> float:
        return self.__value__ + Fraction.getValue(other)

    def __sub__(self, other):
        return self.__value__ - Fraction.getValue(other)

    def __neg__(self):
        return - self.__value__
    
    def __mul__(self, other):
        return self.__value__ * Fraction.getValue(other)

    def __truediv__(self, other):
        return self.__value__ / Fraction.getValue(other)

    def __eq__(self, other):
        return self.getValue() == Fraction.getValue(other)
    
    def __gt__(self, other):
        return self.getValue() > Fraction.getValue(other)

    def __lt__(self, other):
        return self.getValue() < Fraction.getValue(other)

    def __le__(self, other):
        return self.getValue() <= Fraction.getValue(other)

    def __ge__(self, other):
        return self.getValue() >= Fraction.getValue(other)

    def __ne__(self, other):
        return self.getValue() != Fraction.getValue(other)

if __name__ == "__main__":
    a = Fraction(2, 6)
    b = Fraction(2.45)
    print(a) # 1 / 3 = 0.3333333333333333
    print(b) # 49 / 20 = 2.45

    print(a > b) # False

    print(a + b) # 2.783333333333333

    print(a.getValue()) # 0.3333333333333333

    a.setValue(-4, 5)
    print(a) # -4 / 5 = -0.8

    a.setValue(2)
    print(2) # 2