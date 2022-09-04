class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.num = numerator
        self.den = denominator

    def __str__(self) -> str:
        return f'({self.num}/{self.den})'

    def setNum(self, newNum):
        self.num = newNum

    def setDen(self, newDen):
        self.den = newDen

    