print("Bài 5: Class Polynomial")

class Polynomial:
    def __init__(self, lst):
        self.lst = lst
        self.leng = len(lst)
    def __str__(self):
        return "{0}".format(len(self.lst))
    
    @classmethod
    def initializeFromString(self, stringle):
        mang = stringle.split()
        return Polynomial(mang)

    # Các phép toán tử nạp chồng
    def __add__(self, other):
        return self.leng + other.leng
    def __sub__(self, other):
        return self.leng - other.leng
    def __neg__(self):
        return -self.leng
    def __mul__(self, other):
        return self.leng * other.leng
    

polynomialA = Polynomial([1, 2, 3])
polynomialB = Polynomial.initializeFromString('x^4 + 3x^2 - 5x + 1')

polynomialC = polynomialA + polynomialB
print(polynomialC)
polynomialD = polynomialA - polynomialB
polynomialE = -polynomialA
polynomialF = polynomialA * polynomialB
print('polynomialA =', polynomialA)
print('polynomialB =', polynomialB)
print('polynomialC = polynomialA + polynomialB =', polynomialC)
print('polynomialD = polynomialA - polynomialB =', polynomialD)
print('polynomialE = -polynomialA =', polynomialE)
print('polynomialF = polynomialA * polynomialB =', polynomialF)
