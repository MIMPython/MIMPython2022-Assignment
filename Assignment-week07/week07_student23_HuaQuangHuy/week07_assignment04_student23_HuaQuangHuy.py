class Fraction:
    def __init__(self, num, den):
        try:
            if den == 0:
                raise Exception("den == 0")
            self.num = num
            self.den = den
        except Exception:
            print("den is equals 0")

    def __repr__(self):
        return f"{self.num}/{self.den}"

    @staticmethod
    def getBCNN(a, b):
        if a % b == 0:
            return a
        elif b % a == 0:
            return b
        else:
            return a * b

    @staticmethod
    def getGCD(a, b):
        while b != 0:
            c = a % b
            a = b
            b = c

        return a

    @staticmethod
    def getFractionFromFloat(number):
        return Fraction(number * 1000, 1000).reduce()

    def __add__(self, other):
        if self.den == other.den:
            return Fraction(self.num + other.num, self.den)
        else:
            bc = Fraction.getBCNN(self.den, other.den)
            print(bc)
            self.num = self.num * (bc / self.den)
            other.num = other.num * (bc / other.den)
            return Fraction(self.num + other.num, bc)

    def __sub__(self, other):
        if self.den == other.den:
            return Fraction(self.num - other.num, self.den)
        else:
            bc = Fraction.getBCNN(self.den, other.den)
            print(bc)
            self.num = self.num * (bc / self.den)
            other.num = other.num * (bc / other.den)
            return Fraction(self.num - other.num, bc)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def reduce(self):
        gcd = Fraction.getGCD(self.num, self.den)
        self.num = self.num / gcd
        self.den = self.den / gcd
        return self


if __name__ == '__main__':
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(5, 3)
    fraction3 = fraction1 + fraction2
    fraction4 = fraction1 - fraction2
    fraction5 = fraction1 * fraction2
    fraction6 = fraction1 / fraction2
    fraction7 = Fraction.getFractionFromFloat(0.25)
    print(fraction3)
    print(fraction4)
    print(fraction5)
    print(fraction6.reduce())
    print(fraction7)
