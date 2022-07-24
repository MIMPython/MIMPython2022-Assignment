def showA():
    print (f"A = {A}")

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print (f"List ban đầu: A = {A}")

#Câu a
print ("\n(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó")
A[2] = A[2] ** 2
showA()

#Câu b
print ("\n(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau")
print ("Dùng hàm pop")
A.pop(2)
showA()
print ("Dùng hàm del")
del A[2]
showA()

#Câu c
print ("\nThêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A")
A.append(A[len(A)-1] ** 2)
showA()

#Câu d
print (f"\n(d) Tính số phần tử trong list.")
print (len(A))

#Câu e
print (f"\n(e) Tính tổng các phần tử trong list.")
sum = 0
for a in A:
    sum += a
print (sum)

#Câu f
print (f"\n(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.")
sum = A[1] + A[2] + A[3] + A[5]
print (sum)

#Câu g
print (f"\n(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau)")
#Cach1: Cắt (slice)
reversed1_A = A[::-1]
print (f"reversed1_A = {reversed1_A}")
#Cach2: Dung vong lap
reversed2_A = []
for a in A:
    reversed2_A.insert(0, a)
print (f"reversed2_A = {reversed2_A}")

#Câu h
print (f"\n(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.")
odd_A = []
even_A = []
for a in A:
    if a%2 == 0:
        even_A.append(a)
    else:
        odd_A.append(a)
print (f"List số chẵn: even_A = {even_A}")
print (f"List số lẻ: odd_A = {odd_A}")

#Câu i
print(f"\n(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.")
B = sorted(A, reverse=True)
print (f"B = {B}")

#Câu j
print (f"(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.")
if len(A) == len(B):
    print (f"Khi sắp xếp, số phần tử của A và B không thay đổi và bằng {len(A)}")

#Câu k
print (f"(k) Ghép hai list A và list B lại với nhau thành list C.")
C = A + B
print (f"C = {C}")