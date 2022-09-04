import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        else:
            if denominator < 0:
                numerator *= -1
                denominator *= -1
            self.numerator = int(numerator/math.gcd(numerator, denominator))
            self.denominator = int(denominator/math.gcd(numerator, denominator))
    
    @classmethod   
    def initializeFromFloat(cls, num):
        num = str(num)
        nume = int(num.replace(".", ""))
        deno = 10**len(num[num.index(".")+1:])
        return cls(nume, deno)

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"
        
    def __add__(self, other):
        deno = self.denominator * other.denominator
        nume = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(nume, deno)
    
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
        
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        deno = self.denominator * other.denominator
        nume = self.numerator * other.numerator
        return Fraction(nume, deno)
    
    def __truediv__(self, other):
        nume = self.numerator * other.denominator
        deno = self.denominator * other.numerator
        return Fraction(nume, deno)
    
    def __lt__(self, other):
        return self.numerator/self.denominator < other.numerator/other.denominator
    
    def __le__(self, other):
        return self.numerator/self.denominator <= other.numerator/other.denominator
    
    def __eq__(self, other):
        return self.numerator/self.denominator == other.numerator/other.denominator
    
    def __ne__(self, other):
        return self.numerator/self.denominator != other.numerator/other.denominator
    
    def __gt__(self, other):
        return self.numerator/self.denominator > other.numerator/other.denominator
    
    def __ge__(self, other):
        return self.numerator/self.denominator >= other.numerator/other.denominator

if __name__ == "__main__": 
    fractionA = Fraction(11, -25)
    fractionB = Fraction(4, 9)
    print (fractionA) #-11/25
    print (fractionB) #4/9
    print (-fractionA) #11/25
    print (fractionA + fractionB) #1/225
    print (fractionA - fractionB) #-199/225
    print (fractionA * fractionB) #-44/225
    print (fractionA / fractionB) #-99/100
    print (fractionA > fractionB) #False
    print (fractionA < fractionB) #True
    print (fractionA >= fractionB) #False
    print (fractionA <= fractionB) #True
    print (fractionA == fractionB) #False
    print (fractionA != fractionB) #True