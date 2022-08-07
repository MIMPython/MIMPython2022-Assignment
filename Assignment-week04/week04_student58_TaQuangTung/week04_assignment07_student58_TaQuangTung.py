print("Bài 7: Class Polynomial")

class Polynomial:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return Polynomial(self.n + other.n)  
    def __sub__(self, other):
        return Polynomial(self.n - other.n)
    def __sub__(self, other):
        return Polynomial(self.n - other.n)
    def __mul__(self, other):
        return Polynomial(self.n * other.n)
n1 = int(input("polinomialA = "))
polynomialA = Polynomial(n1)
n2 = int(input("polinomialB = "))
polynomialB = Polynomial(n2)

polynomialC = polynomialA + polynomialB
print('polynomialC = polynomialA + polynomialB =', polynomialC.n)
polynomialD = polynomialA - polynomialB
print('polynomialD = polynomialA - polynomialB =', polynomialD.n)
d = Polynomial(0)
polynomialE = d - polynomialA
print('polynomialE = -polynomialA =', polynomialE.n)
polynomialF = polynomialA * polynomialB
print('polynomialF = polynomialA * polynomialB =', polynomialF.n)
