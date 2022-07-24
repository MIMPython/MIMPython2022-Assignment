from msilib.schema import EventMapping


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#câu a
A[2] = A[2]**2
print(A)

#câu b
#cách 1, dùng hàm del
del A[2]
#cách 2, dùng hàm pop
popedA = A.pop(2)

#câu c
ASquare = A[-1]**2
A.append(ASquare)
print(A)

#câu d
count = 0
for ele in A:
    count += 1
print(count)

#câu e
sum = 0
for ele in A:
    sum += ele
print(sum)

#câu f
sum2 = A[1] + A[2] + A[3] + A[5]
print(sum2)

#câu g
#cách 1
reversedA = A[::-1]
print(reversedA)

#cách 2
reversedA2 = reversed(A)
for ele in reversedA2:
    print(ele, end = " ")
    
#câu h
evenNumber = []
oddNumber = []
for ele in A:
    if ele % 2 == 0 :
        evenNumber.append(ele)
    else:
        oddNumber.append(ele)
print(oddNumber)
print(evenNumber)

#câu i
ASorted = sorted(A)
B = ASorted[::-1]
print(B)

#câu j
if len(B) == len(A):
    print("two list have the same length.")
else:
    print("two list don't have the same length.")
    
#câu k
C = A.copy()
for ele in B :
    C.append(ele)
print(C)