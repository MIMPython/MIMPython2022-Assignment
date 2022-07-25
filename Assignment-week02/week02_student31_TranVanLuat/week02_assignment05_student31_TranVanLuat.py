
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A[2] *= A[2]
print(A) #[70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
# Use pop()
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)    # A = [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    
#Use delete()
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2]
print(A)    # A = [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    
#(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
element = A[len(A) - 1]
A.append(element * element)
print(A) # A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

#(d) Tính số phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(len(A)) #15

#(e) Tính tổng các phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum = 0
for i in range(len(A)):
    sum += A[i]
print(sum) #559

#(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sumOfIndex = A[1] + A[2] + A[3] + A[5]
print(sumOfIndex) #173

#(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
#Cach 1
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
newArray = []
for elem in A:
    newArray.append(elem)
newArray.reverse()
print(newArray) #[53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 7, 43, 70]

#Cach 2
Array = []
for index in range(1,len(A)+1):
        Array.append(A[-index])
print(Array) 

#(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
odd_list = []  #lẻ
even_list = [] #chẵn 
for element in A:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)
print(even_list)     # even_number = [70, 46, 34, 80]
print(odd_list)      # odd_number = [43, 7, 77, 35, 49, 3, 1, 5, 53, 3, 53]

#(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = []
for element in A:
    B.append(element)
B.sort()
B.reverse()
print(B)        #[80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]

#(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
print("len(A) == len(B) ?", len(A) == len(B)) #True

#(k) Ghép hai list A và list B lại với nhau thành list C.
C = A + B
print(C) #[70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]