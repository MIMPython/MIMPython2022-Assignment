A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# phần a:
A[2] = A[2] ** 2
print(A) #[70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# phần b:
# Cách 1: 
A.pop(2)
# Cách 2: 
#A.remove(49)
print(A) #[70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# phần c:
A.append(A[len(A)-1]**2)
print(A) #[70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2089]

# phần d:
print(len(A)) #15

#phần e:
sum=0 
for i in A:
    sum+= i

print(sum) #3361

#phần f:
res=0
for i in [1, 2, 3, 5]:
    res += A[i]

print(res) #203

#phần g:
#cách 1:
rever_list=[]
for i in range(len(A)):
    rever_list.append(A[len(A)-1-i])

#cách 2:
rever_list=[]
for item in reversed(A):
    rever_list.append(item)

print(rever_list) #[2089, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 43, 70]

#phần h:
A_chan =[]
A_le = []
for i in A:
    if i%2==1:
        A_le.append(i)
    else:
        A_chan.append(i)
    
print(A_chan) #[70, 46, 34, 80]
print(A_le) #[43, 77, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

#phần i:
B = []
for item in A:
    B.append(item)
B.sort()
B.reverse()
print(B) #[2089, 80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 5, 3, 3, 1]

#phần j:
print(len(A)==len(B))

#phần k:
C=[]
for item in A:
    C.append(item)
for item in B:
    C.append(item)

print(C)