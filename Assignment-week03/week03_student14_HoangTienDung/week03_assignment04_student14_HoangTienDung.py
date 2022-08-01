#C1
def f(x):
	f0 = 0
	f1 = 1
	fn = 1

	if (x < 1):
		return -1
	elif (x == 0 or x == 1):
		return x
	else:
		for i in range(2,x):
			f0 = f1
			f1 = fn
			fn = f0 + f1
		return fn

n = int(input())
print("C1 = " + str(f(n)))

#C2
import sympy
print("C2 = " + str(sympy.fibonacci(n)))