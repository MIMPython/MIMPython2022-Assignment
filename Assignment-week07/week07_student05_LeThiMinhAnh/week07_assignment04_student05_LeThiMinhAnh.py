import fractions
from math import gcd


class Fraction:
    def __init__(self, num, denom):
        self.num = int(num / gcd(abs(num), abs(denom)))
        self.denom = int(denom / gcd(abs(num), abs(denom)))
        if self.denom < 0:
            self.num = -1*self.num
            self.denom = abs(self.denom)
        elif self.denom == 0:
            raise ZeroDivisionError

    def __eq__(self, other):
        return (self.num == other.num and self.denom == other.denom)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.num * other.denom < self.denom * other.num)

    def __le__(self, other):
        return not other < self

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    @classmethod
    def initializeFromFloat(cls, floatNumber):
        frac = str(fractions.Fraction.from_float(
            floatNumber).limit_denominator()).split("/")
        return cls(int(frac[0]), int(frac[1]))

    def __add__(self, other):
        return Fraction(self.num*other.denom + self.denom*other.num, self.denom*other.denom)

    def __repr__(self):
        return "Frac(%s, %s)" % (self.num, self.denom)


if __name__ == "__main__":
    frac1 = Fraction(2, 3)
    frac2 = Fraction.initializeFromFloat(0.42)
    frac3 = Fraction(1, 2)
    print(frac2)  # Frac(21, 50)
    print(frac1 >= frac2)  # True
    print(frac1 + frac2 + frac3)  # Frac(119, 75)
    # Câu hỏi nâng cao. Sau khi đã cài đặt __add__, liệu có thể sử dụng cách viết totalValue = sum([fractionA, fractionB, fractionC]) được hay không?
    print(sum[frac1, frac2, frac3])
    # TypeError: 'builtin_function_or_method' object is not subscriptable
