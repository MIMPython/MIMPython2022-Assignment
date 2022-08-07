polynomialA = int(input())
polynomialB = int(input())

def caculate(a, b):
	c = a + b
	d = a - b
	e = -a
	f = a * b
	print("polynomialC = " + str(c))
	print("polynomialD = " + str(d))
	print("polynomialE = " + str(e))
	print("polynomialF = " + str(f))

caculate(polynomialA, polynomialB)