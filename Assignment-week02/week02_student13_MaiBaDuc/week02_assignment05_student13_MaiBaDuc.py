'''
Bài tập 5. Cho list A với các giá trị dưới đây
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
Hãy thực hiện những yêu cầu sau
(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
(d) Tính số phần tử trong list.
(e) Tính tổng các phần tử trong list.
(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
(k) Ghép hai list A và list B lại với nhau thành list C.
'''
from operator import concat


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

def func_a():
    A[2] = A[2]**2
    print(A)

def func_b():
    #A.pop(2)
    del A[2]
    print(A)

def func_c():
    x=len(A)
    A.append(A[x-1]**2)
    print(A)

def func_d():
    x = len(A)
    print(x)

def func_e():
    S = sum(A)
    print(S)

def func_f():
    sum=0
    x = [1,2,3,5]
    for i in x:
        sum += A[i]

    print(sum)

def func_g():
    B = list(reversed(A))
    C = A[::-1]
    print(B,C)

def func_h():
    even_lst = []
    odd_lst = []
    for i in A:
        if(i%2==0):
            even_lst.append(i)
        else:
            odd_lst.append(i)
    print(even_lst, odd_lst)

def func_i_j_k():
    B = sorted(A, reverse=True)
    print(B)
    print('length of list A: ' + str(len(A)))
    print("length of list B: " + str(len(B)))
    C=A+B
    print(C)
