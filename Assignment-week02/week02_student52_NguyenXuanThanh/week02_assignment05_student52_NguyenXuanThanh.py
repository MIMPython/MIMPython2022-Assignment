# Cho list A với các giá trị dưới đây
# A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# Hãy thực hiện những yêu cầu sau

# (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
# (b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
# (c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
# (d) Tính số phần tử trong list.
# (e) Tính tổng các phần tử trong list.
# (f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
# (g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
# (h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
# (i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
# (j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
# (k) Ghép hai list A và list B lại với nhau thành list C.

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a)
A[2]*= A[2]
print(A[2])#49

#b) 
#cách 1
A.remove(49)
#cách 2
A.pop(2)
print(A) #[70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#c) 
A.append(A[len(A)-1]*A[len(A)-1])
print(A) # [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
#d) 
print(len(A)) # 14 
#e) 
Sum = 0 
for i in A:
    Sum = Sum + i
print(Sum) #3315
#f)
Sum_2 = A[1]+A[2]+A[3]+A[5]
print(Sum_2)#189
#g) 
# cách 1
B = []
i = len(A)-1
while( i > -1):
    B.append(A[i])
    i-=1 
#cách 2
A.reverse()
print(B)#[2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]
print(A)#[2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]

#h)
even = []
odd = []
for i in A:
    if(i % 2 == 1):
        even.append(i)
    else:
        odd.append(i)    
# chẵn        
print(even)#[2809, 53, 3, 53, 5, 1, 3, 49, 35, 77, 43]
# lẻ
print(odd)#[80, 34, 70]
#i)
B=[]
for i in A: 
    B.append(i)
B.sort()
#
print(B) #[1, 3, 3, 5, 34, 35, 43, 49, 53, 53, 70, 77, 80, 2809]

#j 
print(len(A)) # 14
print(len(B)) # 14

#k 
C = A+B
print(C)# [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70, 1, 3, 3, 5, 34, 35, 43, 49, 53, 53, 70, 77, 80, 2809]