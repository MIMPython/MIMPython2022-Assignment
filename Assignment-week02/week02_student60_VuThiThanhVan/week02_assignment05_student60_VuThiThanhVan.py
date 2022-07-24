A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[2]=A[2]**2
length=A[len(A)-1]*A[len(A)-1]
#del A[2]
A.pop(2)

A.append(length)
print(len(A))
sum=0
for i in A:
    sum+=i
print (sum)
sum=A[1]+A[2]+A[3]+A[5]
print(sum)
B=[]
for i in A:
    B.insert(0,i)
print(B)
odd=[]
even=[]
l=len(A)
d=0
for i in A:
    d+=1
    if (d%2==0):
        even.append(i)
    else :
        odd.append(i)
B=A.sort
C=A+B
        


