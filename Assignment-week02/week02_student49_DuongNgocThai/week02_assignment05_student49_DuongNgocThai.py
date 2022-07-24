#Bài 5
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a) 
A[2] = A[2]*A[2]
print(A) #[70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#b)
#Cách 1
A.pop(2)
print(A) #[70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#cách 2
#A.remove(A[2])
#print(A)

#c)
i = len(A) - 1
A.append(A[i]*A[i])
print(A)#70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

#d)
print(len(A))#15

#e) 
print(sum(A))#3361

#f)
sum1 = 0
for i in [1,2,3,5]:
	sum1 = A[i]
print(sum1)#80

#g)
#cách 1
newA = A
newA.reverse()
print(newA)#[2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 43, 70]

'''cách 2
newA = A[::-1]
print(newA)
'''

#h)
chan = []
le = []
for i in A:
	if (i%2 == 0):
		chan.append(i)
	else:
		le.append(i)
print(chan)#[80, 34, 46, 70]
print(le)#[2809, 53, 3, 53, 5, 1, 3, 49, 35, 77, 43]

#i)
B = sorted(A)
print(B)#[1, 3, 3, 5, 34, 35, 43, 46, 49, 53, 53, 70, 77, 80, 2809]

#j)
if (len(A) == len(B)):
	print("Sau khi sắp xếp các phần tử không thay đổi.") #Sau khi sắp xếp các phần tử không thay đổi.

#k)
C = A+B

print(C) #[2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 43, 70, 1, 3, 3, 5, 34, 35, 43, 46, 49, 53, 53, 70, 77, 80, 2809]