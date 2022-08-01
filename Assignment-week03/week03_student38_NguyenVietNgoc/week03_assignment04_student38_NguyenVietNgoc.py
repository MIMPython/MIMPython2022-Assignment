from numpy import mat
import sympy 
import math

# cach 1:
def fibonacci1(n):
	f0 = 0
	f1 = 1
	fn = 1
 
	if (n < 0):
		return "Error"
	elif (n == 0 or n == 1):
		return n
	else:
		for i in range(2, n):
			f0 = f1
			f1 = fn
			fn = f0 + f1
		return fn

# cach 2:
def fibonacci2(n):
	if (n < 0):
		return "Error"
	elif (n == 0 or n == 1):
		return n
	else:
		return fibonacci2(n - 1) + fibonacci2(n - 2)

# cach 3:
def fibonacci3(n):
	phi = (1 + math.sqrt(5)) / 2
	return round(pow(phi, n) / math.sqrt(5))

if __name__ == '__main__':
	print (fibonacci1(9))   # cach 1: 34

	print (fibonacci2(9))   # cach 2: 34
	
	print(fibonacci3(9))    # cach 3: 34

	print (sympy.fibonacci(9))   # cach 4: 34
