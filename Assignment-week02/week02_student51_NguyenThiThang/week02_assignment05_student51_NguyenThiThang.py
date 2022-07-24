A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a
A[2]=A[2]**2
print(A)
#b
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del (A[2])
print(A)
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)
#c
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.append(A[len(A)-1]**2)
print(A)
#d
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("So phan tu trong list A la" , len(A))
#e
sum=0
for i in A:
    sum = sum + i

print("tong cac phan tu cua A la ", sum)
#f
index = [1, 2, 3, 5]
S=0
for i in index:
    S = S + A[i]

print("Tong cac phan tu co chi so 1,2,3,5 la:",S)
#g
B=[]
for i in range(len(A)):
    B.append(A[len(A)-i-1])

print("list A sau khi dao nguoc la: ")
print("Cach 1:",B)
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
newA = A[::-1]
print("Cach 2:",newA)
#h
evenA=[]
oddA=[]
for i in range(len(A)):
    if (A[i] %2==0):
        evenA.append(A[i])
    else:
        oddA.append(A[i])

print("list cac phan tu chan:",evenA)
print("list cac phan tu le:",oddA)

#i
B=sorted(A,reverse=True)
print("list xep theo thu tu giam dan ",B)

#j
if (len(A)==len(B)):
    print("Do dai cua list sau khi sap xep khong thay doi")

#k
C=A +B
print("list C la:",C)

