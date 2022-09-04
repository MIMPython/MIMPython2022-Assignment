import math as m
class InvalidDenominator(Exception):
    pass
class Fraction:
    def __init__(self, a, b):
        try:
            self.a = a
            self.b = b
            if b == 0:
                raise InvalidDenominator
        except InvalidDenominator as e:
            print(str(type(e)) + ' was raised')
    def __str__(self):
        try:
            if self.b != 1 and self.b != 0:
                return str(int(self.a)) + '/' + str(int(self.b)) 
            if self.b == 1 and self.b != 0:
                return str(int(self.a))
            if self.b == 0:
                raise InvalidDenominator
        except InvalidDenominator:
            return 'Can not print invalid fraction'
    def __lt__(self, new_fraction):
        return self.a / self.b < new_fraction.a / new_fraction.b
    def __eq__(self, new_fraction):
        return self.a / self.b == new_fraction.a / new_fraction.b
    def __add__ (self, new_fraction):
        x = self.a * new_fraction.b + new_fraction.a * self.b
        y = self.b * new_fraction.b
        z = m.gcd(x, y)
        return Fraction(x / z, y / z)
    def initializeFromFloat(n):
        cnt = 0
        while n != int(n):
            n *= 10
            cnt += 1
        gcd = m.gcd(int(n), 10 ** cnt)
        return Fraction(n / gcd, (10 ** cnt) / gcd)
if __name__ == '__main__':
    foo = Fraction(2, 3)
    foo1 = Fraction(5, 6)
    print(Fraction(1, 0))
    print(foo + foo1)
    print(Fraction.initializeFromFloat(0.9876))
    print(foo < foo1)