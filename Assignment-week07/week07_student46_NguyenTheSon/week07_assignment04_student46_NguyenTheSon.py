# Bài 4:
import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    @property
    def numerator_fraction(self):
        return self.numerator

    @property
    def denominator_fraction(a):
        return self.denominator

    def __str__(self):  
        return f'{self.numerator // math.gcd(self.numerator, self.denominator)} / {self.denominator // math.gcd(self.numerator, self.denominator)}'
    
    def add(self, another_numerator, another_denominator):
        if math.gcd(another_denominator, self.denominator) == 1:
            return Fraction(self.numerator * another_denominator + another_numerator * self.denominator \
                , another_denominator * self.denominator)
        else: 
            common_denominator = math.lcm(another_denominator, self.denominator)
            a = common_denominator // another_denominator
            b = common_denominator // self.denominator
            return Fraction(self.numerator * b + another_numerator * a \
                , common_denominator)
    
    def Subtraction(self, another_numerator, another_denominator):
        if math.gcd(another_denominator, self.denominator) == 1:
            return Fraction(self.numerator * another_denominator - another_numerator * self.denominator \
                , another_denominator * self.denominator)
        else: 
            common_denominator = math.lcm(another_denominator, self.denominator)
            a = common_denominator // another_denominator
            b = common_denominator // self.denominator
            return Fraction(self.numerator * b - another_numerator * a \
                , common_denominator)
                
    def multiplication(self, another_numerator, another_denominator):
        a = math.gcd(another_numerator, self.denominator)
        b = math.gcd(another_denominator, self.numerator)
        if a > 1:
            another_numerator //= a
            self.denominator //= a
        if b > 1:
            another_denominator //= b
            self.numerator //= b
        return Fraction(another_numerator * self.numerator, another_denominator * self.denominator)
 


if __name__ == '__main__':
    fraction_1 = Fraction(10, 20)             # 1 / 2
    fraction_2 = Fraction(21,50)              # 21 / 50
    fraction_2.add(23,50)                     # 22 / 25 
    fraction_2.Subtraction(23,50)             # -1 / 25
    fraction_2.multiplication(2,3)            # 7 / 25