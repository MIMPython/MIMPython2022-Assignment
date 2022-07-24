from audioop import reverse
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print('Chuỗi ban đầu:',A)
#Câu a
print('\nThay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.')
A[3] = A[3]**2
print(A) 

#Câu b
print('\nXóa phần tử thứ 3 của list A')
#cách 1
A.pop(2)
print(A)

#cách 2
del A[2]
print(A)

#Câu c
A.append(A[-1]**2)
print('\nChuỗi sau khi thêm bình phương phần tử cuối vào:')
print(A)

#Câu d
print('\nSố phần tử của chuỗi là:')
print(len(A))

#Câu e
print ('\nTính tổng các phần tử trong list.')
print(sum(A))


#Câu f
print('\nTổng các phần tử thứ 1,2,3,5 của chuỗi là:')
print(A[1]+A[2]+A[3]+A[5])

#Câu g
print('\nChuỗi đảo ngược:')
#cách 1
new_list1 = list(reversed(A))
print (new_list1)

#cách 2
new_list2 = A[::-1]
print (new_list2)

#Câu h
odd_list = []
even_list = []
for i in A:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f'\nChuỗi lẻ là: {odd_list}')
print(f'\nChuỗi chẵn là: {even_list}')

#Câu i
B = sorted(A,reverse = True)
print ('\nB =',B)

#Câu j
print('\nSo sánh độ dài list A và B có bằng nhau không?')
print(len(A)==len(B))
    
#Câu k
C = A + B
print('\nC=',C)

