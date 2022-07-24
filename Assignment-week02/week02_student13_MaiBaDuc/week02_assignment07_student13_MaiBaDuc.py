'''
Bài tập 7. (Mật mã Caesar)
Trong mã hóa, mật mã Caesar thay thế mỗi kí tự trong bảng chữ cái bởi một kí tự khác cũng trong bảng chữ cái đó ở vị trí cách nó một đoạn cố định.
Hình dưới đây thể hiện mã Caesar ROT-19, khi vòng chữ cái trong được xoay 19 nấc theo chiều dương để tạo ra bảng mã hóa cho vòng chữ cái ngoài. 
Chẳng hạn, kí tự T là mã hóa của kí tự A, kí tự U là mã hóa của kí tự B, … 
Khi đó, nếu thông điệp ban đầu là PYTHON thì thông điệp được mã hóa tương ứng là IRMAHG.
'''
import string
A = list(string.ascii_uppercase)
s = str(input("String: "))
lst = list(s.upper())

def encode():
    i=0
    for i_1 in lst:
        for i_2 in A:
            if(i_2==i_1):
                key = A.index(i_1)
                if(key<=12):
                    lst[i] = A[key+13]
                else:
                    lst[i] = A[key+13-26]
        i += 1
    print(lst)

def decode():
    i=0
    for i_1 in lst:
        for i_2 in A:
            if(i_2==i_1):
                key = A.index(i_1)
                if(key<=12):
                    lst[i] = A[key+26-13]
                else:
                    lst[i] = A[key-13]
        i += 1
    print(lst)

