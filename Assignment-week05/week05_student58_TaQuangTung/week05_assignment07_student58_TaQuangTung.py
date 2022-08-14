print("Bài 7: Palindrome Number")

from math import sqrt

#Kiểm tra số xuôi ngược
def palindrome_check(n):
    stringle = str(n)
    length = len(stringle)
    lst = []        #Mảng chứa các chữ số
    for i in stringle:
        lst.append(i)
    
    #Thử số xuôi ngược
    lst.reverse()
    stringle_new = ""
    for j in lst:
        stringle_new += j
    
    #Thuật toán kiểm tra số xuôi ngược
    if stringle_new == stringle:
        return True
    else:
        return False

def square_number_check(n):
    k = sqrt(n)
    if int(k)**2 == n:
        print(f"Số xuôi ngược {n} là số chính phương")
    else:
        print(f"Số xuôi ngược {n} không là số chính phương")
n = int(input("Nhập số tự nhiên: "))
check = palindrome_check(n)

if check:
    square_number_check(n)
else:
    print("Đây không là số xuôi ngược")

"""
Vẫn còn tồn tại vô số những số xuôi ngược là số chính phương
"""