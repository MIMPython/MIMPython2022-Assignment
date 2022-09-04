
def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n
class Fraction:
    def __init__(self, n, d):
        self.numerator = int(n/gcd(abs(n),abs(d)))
        self.denominator = int(d/gcd(abs(n),abs(d)))
        if self.denominator < 0:
            self.numerator = -(self.numerator)
            self.denominator = abs(self.denominator)
        elif self.denominator == 0:
            raise ZeroDivisionError

    def add(self, other):
        res = Fraction(self.numerator*other.denominator + self.denominator*other.numerator, self.denominator*other.denominator)
        return res
    def sub(self, other):
        res = Fraction(self.numerator*other.denominator - self.denominator*other.numerator, self.denominator*other.denominator)
        return res
    def mul(self, other):
        res = Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
        return res
    def div(self, other):
        res = Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
        return res

    def initializeFromFloat(floatNum):
        frac = float(floatNum).as_integer_ratio()
        return Fraction(frac[0],frac[1])

    def __str__(self): 
        if self.denominator == 1:
            return(str(self.numerator))
        else:
            return '%s/%s' %(self.numerator, self.denominator)

f1 = Fraction(3,4)
print(f1) # 3/4
f2 = Fraction(5,6)
print(Fraction.add(f1, f2)) # 19/12
print(Fraction.initializeFromFloat(0.25)) # 1/4
#f3 = Fraction.initializeFromFloat(0.58)
print(f1 > f2)