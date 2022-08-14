from __future__ import annotations

import copy
import math
from typing import List, Union


class Polynomial:

    def __init__(self, coefficients: List[Union[int, float]]):

        self.coefficients = coefficients
        self.len = len(self.coefficients)

    def __str__(self):
        """Converts a Polynomial into a string"""
        order = self.len - 1
        represent = []
        for coe in self.coefficients:
            if coe == 0:
                continue
            represent.append("- " if coe < 0 else "+ ")
            represent.append(str(format(coe, '.3f')))
            represent.append(" ")
            if order > 0:
                represent.append("z")

            if order > 1:
                represent.append(f"**{order}")

            represent.append(" ")
            order -= 1

        return "".join(represent)[2:-2]

    def __repr__(self):
        return str(self)

    def __neg__(self):
        return Polynomial([-coefficient for coefficient in self.coefficients])

    def __call__(self, value: Union[int, float]) -> Union[int, float]:
        return self.val(value)

    def __add__(self, other: Polynomial) -> Polynomial:
        return self.add(other)

    def __sub__(self, other: Polynomial) -> Polynomial:
        return self.sub(other)

    def __mul__(self, other: Union[int, float, Polynomial]) -> Polynomial:
        return self.mul(other)

    def get_coefficient(self, i: int) -> Union[int, float]:
        """Return the coefficient of the x^i term of polynomial"""
        return self.coefficients[self.len - i - 1]

    def val(self, value: Union[int, float]) -> float:
        """Returns the numerical result of evaluating the polynomial when x equals value"""
        # naive - Time Complexity: O(N)
        # res = 0
        # i = self.len - 1
        # while i >= 0:
        #     res += self.coefficients[i] * value ** (self.len - i - 1)
        #     i -= 1
        #
        # return float(res)

        # Horner's rule - Time Complexity: O(logN)
        res = 0
        for i in range(self.len):
            res = res * value + self.coefficients[i]

        return float(res)

    def add(self, other: Polynomial) -> Polynomial:
        """Returns a new Polynomial representing the sum of Polynomials self and other"""

        large_coefficients = copy.deepcopy(other.coefficients)
        small_coefficients = copy.deepcopy(self.coefficients)

        if self.len > len(other.coefficients):
            large_coefficients = copy.deepcopy(self.coefficients)
            small_coefficients = copy.deepcopy(other.coefficients)


        i, j = len(large_coefficients) - 1, len(small_coefficients) - 1
        while j >= 0:
            large_coefficients[i] += small_coefficients[j]
            i -= 1
            j -= 1

        return Polynomial(large_coefficients)

    def sub(self, other: Polynomial) -> Polynomial:
        """Returns a new Polynomial representing the subtract of Polynomials self and other"""

        minuend = copy.deepcopy(self.coefficients)
        subtrahend = [-coefficient for coefficient in other.coefficients]

        large_coefficients = subtrahend
        small_coefficients = minuend

        if self.len > len(other.coefficients):
            large_coefficients = minuend
            small_coefficients = subtrahend

        i, j = len(large_coefficients) - 1, len(small_coefficients) - 1
        while j >= 0:
            large_coefficients[i] += small_coefficients[j]
            i -= 1
            j -= 1

        return Polynomial(large_coefficients)

    def mul(self, other: Union[int, float, Polynomial]) -> Polynomial:
        """returns a new Polynomial representing the product of Polynomials self and other"""
        if isinstance(other, (int, float)):
            return Polynomial(self._mul_constant(self.coefficients, other))

        multiplicand = copy.deepcopy(self.coefficients)
        multiplier = copy.deepcopy(other.coefficients)

        if self.len < len(other.coefficients):
            multiplicand, multiplier = multiplier, multiplicand

        product = Polynomial([0 for _ in range(len(multiplicand))])
        i = len(multiplier) - 1
        while i >= 0:
            temp_coefficients = self._mul_constant(multiplicand, multiplier[i]) + \
                                [0 for _ in range(len(multiplier) - i - 1)]
            product = product.add(Polynomial(temp_coefficients))
            i -= 1

        return product

    def roots(self) -> Union[List[Union[float, complex]], str]:
        """Returns a list containing the root or roots of first or second order polynomials"""
        if self.len == 2:
            return [-self.coefficients[1] / self.coefficients[0]]
        if self.len == 3:
            a, b, c = self.coefficients[0], self.coefficients[1], self.coefficients[2]
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                x1 = (-b - complex(delta) ** 0.5) / (2 * a)
                x2 = (-b + complex(delta) ** 0.5) / (2 * a)
                return [x1, x2]
            elif delta == 0:
                return [-b / (2 * a)]
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)

            return [x1, x2]
        if self.len == 1:
            return "The equation has no roots"

        return "Order is too high to find the roots"

    @staticmethod
    def _mul_constant(poly: List[Union[int, float]], const: Union[int, float]) \
            -> List[Union[int, float]]:
        return [coefficient * const for coefficient in poly]

if __name__ == '__main__':
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([100, 200])
    print(p1)  # 1.000 z**2 + 2.000 z + 3.000
    print(p1.add(p2))  # 1.000 z**2 + 102.000 z + 203.000
    print(p1 + p2)  # 1.000 z**2 + 102.000 z + 203.000
    print(p1(1))  # 6.0
    print(p1(-1))   # 2.0
    print((p1 + p2)(10))  # 1323.0
    print(p1.mul(p1))   # 1.000 z**4 + 4.000 z**3 + 10.000 z**2 + 12.000 z + 9.000
    print(p1 * p1)  # 1.000 z**4 + 4.000 z**3 + 10.000 z**2 + 12.000 z + 9.000
    print(p1 * p2 + p1)     # 100.000 z**3 + 401.000 z**2 + 702.000 z + 603.000
    print(p1.roots())   # [(-1-1.4142135623730951j), (-0.9999999999999999+1.4142135623730951j)]
    print(p2.roots())   # [-2.0]
    p3 = Polynomial([3, 2, -1])
    print(p3.roots())   # [-1.0, 0.3333333333333333]
    print((p1 * p1).roots())    # Order is too high to find the roots
    print(-p1)  # -1.000 z**2 - -2.000 z - -3.000
