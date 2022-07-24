
#    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a. Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[2] = A[2]**2
print(A)
#b. Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
    #1 - Sử dụng hàm delete
del A[2]
print(A)
    #2 - sử dụng hàm pop
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)

#c. Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
i = len(A)-1
A.append(A[i])
print(A)

#d. Tính số phần tử trong list.
    #1 - using len() method
print(len(A))
    #2
count = 0
for item in A:
    count = count + 1
print(count)

#(e) Tính tổng các phần tử trong list.
sum = 0
for item in A:
    sum = sum + item
print(sum)

#(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
sum = A[1] + A[2] + A[3] +A[5]
print(sum)

#(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
    #1 - using reverse() method
A.reverse()
print(A)
    #2

    new = A[:]
    length = len(A)
    i=0
    while i < length:
        new[i] = A[length-1-i]
        i+=1
    print(new)

#(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
even = []
odd = []
for i in A:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


#(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = []
A.sort()
A.reverse()
B = A[:]
print(B)

#(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
if len(A) == len(B):
    print('length of A = length of B')
else:
    print('length of A is not equal length of B')

#(k) Ghép hai list A và list B lại với nhau thành list C.
A.extend(B)
print(A)