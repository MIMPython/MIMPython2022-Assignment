class Polynomial:
    def __init__(self, coefficients):
        coefficients = [float(ele) for ele in coefficients]
        self.coefficients = coefficients
        
    def __repr__(self):
        return f"Polynomial({self.coefficients})"
    
    def __add__(self, other):
        newPoly = []
        selfCoeffs = self.coefficients
        otherCoeffs = other.coefficients
        diff = len(selfCoeffs) - len(otherCoeffs)
        if diff < 0:
            selfCoeffs = [0] * abs(diff) + selfCoeffs
        else:
            otherCoeffs = [0] * abs(diff) + otherCoeffs
        for i in range (len(selfCoeffs)):
            newPoly.append(selfCoeffs[i] + otherCoeffs[i])
        return Polynomial(newPoly)
    
    def __neg__(self):
        negPoly = [-ele for ele in self.coefficients]
        return Polynomial(negPoly)
    
    def __sub__(self, other):
        return self + (-other)
                
    def __mul__(self, other):
        selfDegree = len(self.coefficients) - 1
        otherDegree = len(other.coefficients) - 1
        newDegree = selfDegree + otherDegree
        newPoly = [0] * (newDegree + 1)
        for i in range (len(self.coefficients)):
            for j in range(len(other.coefficients)):
                newPoly[newDegree - (selfDegree - i) - (otherDegree - j)] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(newPoly)

    @classmethod
    def initializeFromString(cls, poly:str):
        coeffsDict = {}
        polySplit = poly.split(" ")
        while "+" in polySplit:
            pos = polySplit.index("+")
            polySplit[pos+1] = "+" + polySplit[pos+1]
            polySplit.remove("+")
        while "-" in polySplit:
            pos = polySplit.index("-")
            polySplit[pos+1] = "-" + polySplit[pos+1]
            polySplit.remove("-")
        for ele in polySplit:
            if "^" in ele:
                exp = int(ele[ele.index("^")+1:])
                if ele.index("x") == 0:
                    coeffsDict[exp] = 1
                else:
                    coeff = ele[:ele.index("x")]
                    if coeff == "-":
                        coeffsDict[exp] = -1
                    else:
                        coeffsDict[exp] = float(coeff)
            else:
                if "x" in ele:
                    if ele.index("x") == 0:
                        coeffsDict[1] = 1
                    else:
                        coeff = ele[:ele.index("x")]
                        if coeff == "-":
                            coeffsDict[1] = -1
                        else:
                            coeffsDict[1] = float(coeff)
                else:
                    coeffsDict[0] = float(ele)
        newPoly = []
        for i in range(max(coeffsDict.keys()), -1, -1):
            if i not in coeffsDict.keys():
                newPoly.append(0)
            else:
                newPoly.append(coeffsDict[i])
        return cls(newPoly)
    
def main():    
    polynomialA = Polynomial([1, 2, 3])
    print(polynomialA) #Polynomial([1.0, 2.0, 3.0])
    polynomialB = Polynomial.initializeFromString('x^4 + 3x^2 - 5x + 1')
    print(polynomialB) #Polynomial([1.0, 0.0, 3.0, -5.0, 1.0])
    
    polynomialC = polynomialA + polynomialB
    print(polynomialC) #Polynomial([1.0, 0.0, 4.0, -3.0, 4.0])
    polynomialD = polynomialA - polynomialB
    print(polynomialD) #Polynomial([-1.0, 0.0, -2.0, 7.0, 2.0])
    polynomialE = -polynomialA
    print(polynomialE) #Polynomial([-1.0, -2.0, -3.0])
    polynomialF = polynomialA * polynomialB
    print(polynomialF) #Polynomial([1.0, 2.0, 6.0, 1.0, 0.0, -13.0, 3.0])

if __name__ == "__main__":
    main()