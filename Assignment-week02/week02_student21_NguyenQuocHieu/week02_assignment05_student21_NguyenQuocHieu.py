A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("A: ", A)
def createArray():
    B = []
    index = 0
    while (index < len(A)):
        B.append(A[index])
        index = index + 1
    return B
# a,
Aa = createArray()
valueAa = int(Aa[2])
valueAa = valueAa ** 2
Aa.pop(2)
Aa.insert(2, valueAa)
print("Result in a: ", Aa)
# b,
Ab1 = createArray()
Ab1.pop(2)
print("First solution in b: ", Ab1)
Ab2 = []
Ab2.append(A[0])
Ab2.append(A[1])
index = 2
while int(index) < len(A):
    Ab2.append(A[int(index)])
    index = int(index) + 1
print("Second solution in b: ", Ab2)
# c, 
valueLast = int(A[len(A) - 1])
valueLast = valueLast ** 2
Ac = createArray()
Ac.append(valueLast)
print("Result in c: ", Ac)
# d,
number = len(A)
print("Number of elements in A: ", number)
# e, 
sum = 0
for element in A:
    sum = sum + int(element)
print("Total of all elements in A:", sum)
# f, 
sum2 = int(A[1]) + int(A[2]) + int(A[3]) + int(A[5])
print("Total of first, second, third and fifth elements in A: ", sum2)
# g, 
Ag1 = createArray()
Ag1.reverse()
print("First solution in g: ", Ag1)
Ag2 = []
i = 0
while (i < len(A)):
    Ag2.append(A[len(A) - 1 - i])
    i = i + 1
print("Second solution in g: ", Ag2)
# h,
AhEven = []
AhOdd = []
j = 0
while(j < len(A)):
    if (int(A[j]) % 2 == 0):
        AhEven.append(A[j])
    else: 
        AhOdd.append(A[j])
    j = j + 1
print("Even list: ", AhEven)
print("Odd list: ", AhOdd)
# i,

