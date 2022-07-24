from math import sqrt
print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
c = float(input("Nhập số c = "))

def solve(a, b, c):
	if(a==0):
		if(b==0):
			if(c==0):
				print("Phương trình vô số nghiệm!")
			else:
				print("()")
		else:
			if(c==0):
				print("0")
			else:
				print(str(-b/c))

	else:
		delta = b ** 2 - 4 * a * c
		if(delta==0):
			print(str(-b/(2*a)))
		elif(delta > 0):
			print(str((-b-sqrt(delta))/(4*a)) + ", " + str((-b+sqrt(delta))/(4*a)))
		else:
			print("()")

solve(a, b, c)