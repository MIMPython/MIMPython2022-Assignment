"""
nummpy.linspace
"""

# Explanation & examples

"""
numpy.polyval(p, x):
    - Evaluate a polynomial at specific values.
    - Parameters:
        + p: a 1-D array of the length n+1
        (the polynomial described as
        p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n])
        + x: a nunmber, or an array of numbers, or a polynomial 
        (when x is a polynomial, the function return p(x(t))).

Example:
>>> numpy.polyval([5,6,1],10)
561
>>> numpy.polyval([5,6,1],[10,11])
array([561, 672])
>>> numpy.polyval([5,6,1], numpy.poly1d([2,1]))
poly1d([20, 32, 12])
"""

# Program does the same actions

import numpy, time


def myPolyval(p: list, x):
    """
    p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
    """
    if type(x) == int or type(x) == float:
        polynomialValue = 0
        for index in range(1, len(p) + 1):
            polynomialValue += p[index - 1] * x ** (len(p) - index)
        return polynomialValue
    elif type(x) == list:
        polynomialValueArray = []
        polynomialValue = 0
        for i in range(len(x)):
            for index in range(1, len(p) + 1):
                polynomialValue += p[index - 1] * x[i] ** (len(p) - index)
            polynomialValueArray.append(polynomialValue)
            polynomialValue = 0
        return polynomialValueArray
    elif type(x) == numpy.poly1d:
        pass  # don't know how to do without numpy :D
    else:
        return "Invalid input"


# print(myPolyval([5, 6, 1], 10))
# print(myPolyval([5, 6, 1], [10, 11]))
# print(myPolyval([5, 6, 1], {10}))

# Comparing 2 methods

examplePolynomial = numpy.random.randint(2**31, size=50)
exampleArray = list(numpy.random.randint(2**31, size=10))

startTime1 = time.time()
result1 = myPolyval(examplePolynomial, exampleArray)
print(result1)
stopTime1 = time.time()
myMethodTime = stopTime1 - startTime1

startTime2 = time.time()
result2 = numpy.polyval(examplePolynomial, exampleArray)
print(result2)
stopTime2 = time.time()
numpyMethodTime = stopTime2 - startTime2

print(f"My method: {myMethodTime}")
print(f"Numpy method: {numpyMethodTime}")

with open(
    ".\\additionalFolder\\week06_assignment02_student28_MaiThanhLiem_data.md", "a"
) as function:
    """
    | My method | Numpy method |
    | :-------: | :----------: |
    """
    function.write(f"|{myMethodTime}|{numpyMethodTime}|\n")
