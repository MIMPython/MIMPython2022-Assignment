class Polynomial:
    def __init__(self, coefs):
        """
        P(x) = coef[0]x^n + ... coef[n-1]x + coef[n]
        def(P(x)) = len(coefs) - 1
        """
        self.coefs = coefs

    def strip(self):
        for i in range(len(self.coefs)):
            while not self.coefs[i]:
                self.coefs.pop(self.coefs[i])
            break

    def __repr__(self):
        Polynomial.strip(self)
        return f"Polynomial{(self.coefs)}"

    def __add__(self, another):
        Polynomial.strip(self)
        Polynomial.strip(another)
        newDegree = max(len(self.coefs), len(another.coefs)) - 1
        newCoefs = []
        while len(self.coefs) < newDegree + 1:
            self.coefs.insert(0, 0)
        while len(another.coefs) < newDegree + 1:
            another.coefs.insert(0, 0)
        for i in range(newDegree + 1):
            newCoef = self.coefs[i] + another.coefs[i]
            newCoefs.append(newCoef)
        return Polynomial(newCoefs)

    def __radd__(self, another):
        return self.__add__(another)

    def __sub__(self, another):
        Polynomial.strip(self)
        Polynomial.strip(another)
        newDegree = max(len(self.coefs), len(another.coefs)) - 1
        newCoefs = []
        while len(self.coefs) < newDegree + 1:
            self.coefs.insert(0, 0)
        while len(another.coefs) < newDegree + 1:
            another.coefs.insert(0, 0)
        for i in range(newDegree + 1):
            newCoef = self.coefs[i] - another.coefs[i]
            newCoefs.append(newCoef)
        return Polynomial(newCoefs)

    def __rsub__(self, another):
        newPolynomial = self.__sub__(another)
        for i in range(len(newPolynomial.coefs)):
            newPolynomial.coefs[i] = -newPolynomial.coefs[i]
        return Polynomial(newPolynomial.coefs)

    def __mul__(self, another):
        Polynomial.strip(self)
        Polynomial.strip(another)
        newDegree = (len(self.coefs) - 1) + (len(another.coefs) - 1)
        newCoefs = [0] * (newDegree + 1)
        for i in range(newDegree + 1):
            for j in range(len(self.coefs)):
                for k in range(len(another.coefs)):
                    if (j + k) == i:
                        newCoefs[i] += self.coefs[j] * another.coefs[k]
        return Polynomial(newCoefs)

    def __rmul__(self, another):
        return self.__mul__(another)

    @property
    def degree(self):
        Polynomial.strip(self)
        return len(self.coefs) - 1


if __name__ == "__main__":
    P = Polynomial([0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 2, 3])
    Q = Polynomial([1, 4, 6, 10])
    print(P, "\n", P.degree)
    print(Q, "\n", Q.degree)
    print(P + Q)
    print(Q + P)
    print(P - Q)
    print(Q - P)
    print(P * Q)
    print(Q * P)
