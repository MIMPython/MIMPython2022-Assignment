print("Cho list A các giá trị dưới đây:")
print("A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#câu a)
A[3] = 46**2
print("Câu a) List A sau khi giá trị thứ ba được thay thế bởi bình\
 phương của chính nó là")
print(A)

#câu b (Cách 1)
del A[3]
print ("Câu b) List A sau khi giá trị thứ ba bị loại bỏ là")
print("Hàm delete:", A)

#Câu b (Cách 2)
bi_loai = A.pop(int(3))
print("Hàm pop():", A)

#Câu c)
them_vao = 53**2
A.insert(16, them_vao)
print("Câu c) List A sau khi thêm vào bình phương thành phần cuối là:")
print(A)

#Câu d)
print("Câu d) Số thành phần trong list A là:", len(A))

#Câu e)
print("Câu e: Tổng của các phần tử trong list là:", sum(A))

#câu f)
t1 = A.pop(int(1))
t2 = A.pop(int(1))
t3 = A.pop(int(1))
t5 = A.pop(int(1))

A2 = [t1, t2, t3, t5]
print("Câu f: Tổng của các thành phần 1,2,3,5 là:", sum(A2))

#Câu g)
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.reverse()
print("Câu g: List A sau khi đảo ngược vị trí của các thành phần là:", A)

#Câu h)
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

day_so_le = sorted([i for i in A if i % 2 ==0])
day_so_chan = sorted([i for i in A if i % 2 ==1])

print("Câu h:")
print("Dãy số lẻ trích ra từ list A là:", day_so_le)
print("Dãy số chẵn trích ra từ list A là:", day_so_chan)

#Câu i)
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

A.sort(reverse = True)

print("Câu i: List A theo thứ tự giảm dần từ trái qua phải là:",A)
print("Ta gọi dãy số trên là dãy B")
#Câu j:
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

def thutu(A):
    return sorted(A)

print("Độ dài dãy A là:", len(A))
print("Độ dài dãy B là:", len(thutu(A)))
print("Hiệu độ dài của hai dãy là:", len(A) - len(thutu(A)))
print("Suy ra: số phần tử của dãy sau khi sắp xếp là không đổi.")

#Câu k:
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

B = [80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]

list = A + B
print("Hai list sau khi được ghép với nhau là:")
print(list)

