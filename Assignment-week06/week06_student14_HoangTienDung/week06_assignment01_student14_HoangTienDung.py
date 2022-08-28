#a
import random
def foo(x, y):
	a = []
	for i in range(0, x):
		b = []
		for j in range(0, y):
			n = random.randint(1, 9)
			b.append(n)
		a = a + [b]
	return a

m = int(input("Nhập m = "))
n = int(input("Nhập n = "))
array = foo(m, n)
for i in range(0, m):
	for j in range(0, n):
		print(array[i][j], end = ' ')
	print()	

#b
def sum(a):
	res = []
	for j in range(0, len(a[0])):
		t = 0
		for i in range(0, len(a)):
			t = t + a[i][j]
		res.append(t)
	print(res)
sum(array)