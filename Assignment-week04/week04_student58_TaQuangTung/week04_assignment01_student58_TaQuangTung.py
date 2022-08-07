print("Bài 1: Sort A List")
print()
#List con ổn

maxrow = int(input("Nhập độ dài của list A: "))
Ai = []         #List theo các hàng lớn
A = []      

for hang in range(maxrow):
    x = int(input(f"Nhập số lượng phần tử của hàng thứ {hang}: "))
    Ai.append(x)        
print("Chuyển sang các phần tử trong list con")
for cot in range(maxrow):
    lst = []
    for j in range(Ai[cot]):
        x = int(input(f"Phần tử thứ {j} của hàng thứ {cot} là: "))
        lst.append(x)
    A.append(lst)

#Mảng A ban đầu INPUT: A = [[1, 2], [3, 0, 4], [2], [4, 5]]
print("A = ", A)
#Mảng B in ra OUTPUT
B = []
dictor = dict()         #dictionary
do_dai = len(A)         #Độ dài mảng A

#Tính tổng qua các phần tử trong A qua dictionary
for i in range(do_dai):
    dictor[i] = sum(A[i])

#Sắp xếp thông qua giá trị
lst = sorted(dictor.values())

#List gồm chỉ số đã được sắp xếp
ln = []
for j in range(do_dai):
    for key, val in dictor.items():
        if val == lst[j]:
            ln.append(key)

for k in ln:
    B.append(A[k])
print("B = ", B)


#Yêu cầu bổ sung: So sánh hai list ổn bất kỳ 
if A == B:
    print("Đây là hai list ổn")
else:
    print("Đây là hai list không ổn")
