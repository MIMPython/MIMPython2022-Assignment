def snt(x):
	uoc = 0
	for i in range(1,x+1):
		if ((x % i) == 0):
			uoc += 1
	if (uoc == 2):
		return True
	else:
		return False		

P = []
for i in range(1, 600851475144):
	if ((600851475143 % i) == 0):
		if (snt(i) == True):
			P.append(i)

print(max(P))