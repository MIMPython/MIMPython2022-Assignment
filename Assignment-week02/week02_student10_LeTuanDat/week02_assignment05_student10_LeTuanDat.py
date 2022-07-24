a) A[2] *= A[2]
b) del A[2]
   A.pop(2)
c) lastElement = A[len(A)-1]
   A.append(lastElement**2)
d) numberOfList = len(A)
e) sumOfElements = 0
for element in A
	sumOfElements += element
print(sumOfElement)
f) sumOfDesignatedElement = A[1] + A[2] + A[3] + A[5]
print(sumOfDesignatedElement)
g) Way1: newList = []
for element in A
	newList.append(element)
newList.reverse()
   
   Way2: newList2 = []
for index in range(1, len(A) + 1)
	newList2.append(A[-index])
print(newList2)
h) evenNumberList = []
   oddNumberList = []
for element in A
	if element % 2 == 0:
		evenNumberList.append(element)
	else:
		oddNumberList.append(element)
i) B = []
for element in A
	B.append(element)
b.sort()
B.reverse()
j) print(len(A) == len(B))
k) C = A + B
