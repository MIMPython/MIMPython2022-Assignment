'''
Xây dựng class Polynomial sao cho có thể thực hiện các phép toán cộng (+), trừ (−), nhân (∗) giữa hai instance của class này
'''

class Polynomial:
    def __init__(self, coefficient):
        self.coeff = coefficient

    def getCoefficient(self):
        return self.coeff

    # Phep cong:

    def add(self, other):
        maxOfDegree = max(len(self.getCoefficient()),len(other))
        result = [0]*maxOfDegree

        for i in range(maxOfDegree):
            result[i] = ((self.getCoefficient())[i] + other[i])
        return result
    
    # Phep tru:

    def sub(self, other):
        maxOfDegree = max(len(self.getCoefficient()), len(other))
        result = [0]*maxOfDegree

        for i in range(maxOfDegree):
            result[i] = ((self.getCoefficientI())[i] - other[i])
        return result

    # Phep nhan:

    # Phep chia: 

def presentPolynomial(coefficient, x):
    return sum((a*x**i) for i, a in enumerate(coefficient)) #enumerate() returns (index, corresponding value)

# Thuc hien phep cong polynomialA + polynomialB:
if __name__ == '__main__':
    listOfCoeffA = [1,2,3]
    listOfCoeffB = [2,0,5]
    polynomialA = Polynomial(listOfCoeffA)
    polynomialB = Polynomial(listOfCoeffB)
    sum = polynomialA.add(listOfCoeffB) 
    print(sum) #[3, 2, 8]


    