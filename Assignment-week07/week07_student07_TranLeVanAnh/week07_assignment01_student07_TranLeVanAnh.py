#Bai1
A=[]
a = int(input("Nhập độ dài của mảng "))
for i in range(a):
    try:
        b = int(input())
        A.append(b)
    except:
        print("ERROR")
def func(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    print("Giá trị trung bình của danh sách đó là", sum/len(A))
func(A)