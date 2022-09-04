class Fraction:
    def __init__(self, numerator, denominator, number):
        self.numerator = numerator
        self.denominator = denominator
        self.number = number

    def getValue(self):
        return self.numerator / self.denominator

    def initializeFromFloat(self):
        if '.' in str((self.number)):
            return 'frac ' + str(int(float(self.number)*10**(len(str(self.number)) - 1 - str(self.number).find('.')))) + '/' + str(10**(len(str(self.number)) - 1 - str(self.number).find('.')))

a = Fraction(2, 3, 0.88).getValue()
b = Fraction(2, 3, 0.88).initializeFromFloat()
print(a)
print(b)