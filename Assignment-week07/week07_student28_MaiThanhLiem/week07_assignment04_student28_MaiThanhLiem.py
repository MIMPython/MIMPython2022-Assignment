import numpy


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        fracGCD = numpy.gcd(self.numerator, self.denominator)
        self.numerator //= fracGCD
        self.denominator //= fracGCD
        return Fraction(self.numerator, self.denominator)

    def __repr__(self):
        self = Fraction.simplify(self)
        return f"Fraction({self.numerator}/{self.denominator})"

    def __add__(self, another):
        newNumer = (
            self.numerator * another.denominator + self.denominator * another.numerator
        )
        newDenom = self.denominator * another.denominator
        self = Fraction.simplify(self)
        return Fraction(newNumer, newDenom)

    def __radd__(self, another):
        return self.__add__(another)

    def __sub__(self, another):
        newNumer = (
            self.numerator * another.denominator - self.denominator * another.numerator
        )
        newDenom = self.denominator * another.denominator
        self = Fraction.simplify(self)
        return Fraction(newNumer, newDenom)

    def __rsub__(self, another):
        newFrac = self.__sub__(another)
        return Fraction(-newFrac.numerator, -newFrac.denominator)

    def __mul__(self, another):
        newNumer = self.numerator * another.numerator
        newDenom = self.denominator * another.denominator
        self = Fraction.simplify(self)
        return Fraction(newNumer, newDenom)

    def __rmul__(self, another):
        return self.__mul__(another)

    def __truediv__(self, another):
        self = Fraction.simplify(self)
        return self.__mul__(another.inverse)

    def __rtruediv__(self, another):
        return self.__div__(another).inverse

    @property
    def inverse(self):
        return Fraction(self.denominator, self.numerator)


if __name__ == "__main__":
    F = Fraction(2, 3)
    G = Fraction(5, 9)
    print(F)
    print(G)
    print(F + G)
    print(G + F)
    print(F - G)
    print(G - F)
    print(F * G)
    print(G * F)
    print(F / G)
    print(G / F)
    H = Fraction(9, 11)
    someFrac = [F, G, H]
    print(someFrac)
    print(sum(someFrac))
