import math

class Fraction:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def initializeFromFloat(float):
        float_str = str(float)
        digits_after_decimal_points = len(float_str) - 2
        temp = math.gcd(int(float * (10**digits_after_decimal_points)), 10**digits_after_decimal_points)
        numerator = int(float * (10**digits_after_decimal_points)) // temp
        denominator = 10**digits_after_decimal_points // temp
        return f'Frac({numerator},{denominator})'

bar = Fraction.initializeFromFloat(0.42)
print(bar)
