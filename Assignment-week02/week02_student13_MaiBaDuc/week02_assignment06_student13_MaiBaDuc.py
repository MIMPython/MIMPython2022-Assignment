'''
Bài tập 6. Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình
ax2+bx+c=0.ax2+bx+c=0.
Input: ba số a, b, c bất kỳ
Output: một tuple chứa tất cả các nghiệm thực (phân biệt), xếp theo thứ tự tăng dần, của phương trình ax2+bx+c=0.ax2+bx+c=0.
Ví dụ
foo(1, 1, -2) # (-2, 1)
foo(1, 2, 1) # (-1, )
foo(1, 0, 1) # ()
Chú ý.
•	Có thể tạo nhiều hàm con để thực hiện các công việc khác nhau bổ trợ cho hàm chính.
•	Hàm chính chỉ trả về tuple được yêu cầu, không in thêm bất cứ thông tin gì trong quá trình tính toán.

'''
from cmath import sqrt
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2-4*a*c
if(delta>0):
    x_1 = (-b+sqrt(delta))/(2*a)
    x_2 = (-b-sqrt(delta))/(2*a)
    result = (x_1.real,x_2.real)
    result = sorted(result)
    result = tuple(result)
    print(result)
elif(delta==0):
    x = (-b)/(2*a)
    y = (x,)
    y = tuple(y)
    print(y)
else:
    x = ()
    x = tuple(x)
    print(x)