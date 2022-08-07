class Polynomial:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num
    
    def __neg__(self):
        return -self.num
    
def main():
    polynomialA = Polynomial(10)
    polynomialB = Polynomial(30)
    polynomialC = polynomialA + polynomialB
    print(polynomialC)
    polynomialD = polynomialA - polynomialB
    print(polynomialD)
    polynomialE = -polynomialA
    print(polynomialE)
    polynomialF = polynomialA * polynomialB
    print(polynomialF)
    
if __name__ == "__main__":
    main()