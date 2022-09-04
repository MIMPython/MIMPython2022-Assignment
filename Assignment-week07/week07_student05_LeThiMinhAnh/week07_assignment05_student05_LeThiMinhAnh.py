from itertools import zip_longest


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        string = ""
        for i in range(len(self.coefficients)):
            i_coeff = str(self.coefficients[i])
            if i == len(self.coefficients) - 1:
                string += i_coeff
            else:
                if i_coeff == "1":
                    i_coeff = ""
                elif i_coeff == "-1":
                    i_coeff = "-"
                elif i_coeff == "0":
                    continue
                if i < len(self.coefficients) - 2:
                    string += i_coeff + "x^" + \
                        str(len(self.coefficients) - i - 1) + " + "
                elif i < len(self.coefficients) - 1:
                    string += i_coeff + "x" + " + "
        return string.replace("+ -", "- ")

    def __repr__(self):
        return str(self)

    @classmethod
    def initializeFromString(cls, str):
        if "-" in str:
            str = str.replace("- ", "+ -")
        lst = str.split(' + ')
        results = []
        for i in lst:
            i_coeff = i.split("x")[0]
            if i_coeff == "":
                i_coeff = "1"
            results.append(int(i_coeff))
        return cls(results)

    def __add__(self, other):
        coeff1 = self.coefficients[::-1]
        coeff2 = other.coefficients[::-1]
        results = [sum(t) for t in zip_longest(coeff1, coeff2, fillvalue=0)]
        return Polynomial(results[::-1])

    def __sub__(self, other):
        coeff1 = self.coefficients[::-1]
        coeff2 = other.coefficients[::-1]
        results = [t1-t2 for t1,
                   t2 in zip_longest(coeff1, coeff2, fillvalue=0)]
        return Polynomial(results[::-1])

    def __neg__(self):
        newCoeffs = []
        for i in self.coefficients:
            newCoeffs.append(-i)
        return Polynomial(newCoeffs)

    def __mul__(self, other):
        results = Polynomial([0])
        coeff1 = self.coefficients[::-1]
        coeff2 = other.coefficients[::-1]
        for i in range(len(coeff1)):
            if i == 0:
                newCoeffs = [r * coeff1[i] for r in coeff2]
            else:
                newCoeffs = [0] * i + [r * coeff1[i] for r in coeff2]
            results += Polynomial(newCoeffs[::-1])
        return results


def main():
    polynomialA = Polynomial([1, 2, 3])
    print(polynomialA)  # x^2 + 2x + 3
    polynomialB = Polynomial.initializeFromString('x^4 + 3x^2 - 5x + 1')
    polynomialC = polynomialA + polynomialB
    print(polynomialC)  # x^3 + 4x^2 - 3x + 4
    polynomialD = polynomialA - polynomialB
    print(polynomialD)  # -x^3 - 2x^2 + 7x + 2
    polynomialE = -polynomialA
    print(polynomialE)  # -x^2 - 2x - 3
    polynomialF = polynomialA * polynomialB
    print(polynomialF)  # x^5 + 5x^4 + 4x^3 - 13x + 3


if __name__ == "__main__":
    main()
