"""Ta sẽ sử dụng các kiến thức số học để thực hiện 
các yêu cầu của bài toán mà không phải tính n! trực tiếp!"""
"""Với mỗi số nguyên dương n và số nguyên tố p, ta gọi v_p(n) là số nguyên
không âm lớn nhất thỏa p^(v_p(n)) là ước của n. Ta gọi s_p(n) là tổng các chữ số
của n khi viết dưới hệ cơ số p.
Ta có kết quả sau v_p(n) = (n - s_p(n))/(p-1).
Hơn nữa, nếu p < q và p, q là hai số nguyên tố thì v_p(n) < v_q(n)
Cho trước số nguyên dương n.
Câu a).
    Yêu cầu bài toán tương đương với tìm số nguyên m lớn nhất sao cho 10^m là ước của n!
    Do định lý cơ bản của số học thì n! có thể phân tích thành tích của các số nguyên tố
    Viết n! = 2^a.5^b.N với a = v_2(n!), b = v_5(n!) và gcd(N,10) = 1
    Chú ý là v_5(n!) < v_2(n!) nên số nguyên dương m cần tìm chính là v_5(n!)
    
Câu b)
    Với số m tìm được ở câu a) thì ta cần tìm chữ số tận cùng bên phải của n/10^m.
    Hay cũng chính là tìm số dư của số mới khi chia cho 10.
    Theo định lý thặng dư trung hoa thì điều này tương đương với tìm số dư của số này khi chia cho 2 và 5.
    Ta chú ý là v_5(n!) < v_2(n!) nên số mới này luôn là số chẵn.
    Vậy ta chỉ cần xác định số dư của số mới khi chia cho 5 và sử dụng định lý thặng dư trung hoa để
    tìm lại được số dư của số này khi chia cho 10.
    Ta có kết quả sau: Giả sử n có dạng a_{k}.....a_{1}a_{0} khi viết dưới hệ cơ số 5
    Khi đó số dư của n! đồng dư (-1)^{v_5(n!)}.(a_{0}!).(a_{1}!)...(a_{k-1}!).2^(4 - r_4(v_5(n!))) (mod 5)
    trong đó r_4(v_5(n!)) là số dư của v_5(n!) khi chia cho 4.
    Như vậy ta chỉ cần viết n dưới hệ cơ số 5 là có thể dễ dàng tính được v_5(n!) theo công thức đã nêu ở câu a)
    Từ đó dễ dàng tìm ra r_4(v_5(n!)) và cũng tính được tích của các a_{i}!.

     """


"""Hàm tính giai thừa"""
from math import factorial

"""Hàm đổi sang hệ cơ số 5"""

def convert_to_base_5(n):
    num = []
    while n > 0:
        num.insert(0,int(n%5))
        n = (n - n%5)/5
    string = ""
    for i in num:
        string += str(i)
    return(string)
"""Chú ý hai hàm đổi hệ cơ số ta vừa định nghĩa trả cho ta kết quả dạng string"""

"""Hàm tính v_5(n!)"""


def v_5_factorial(n):
    s_5 = 0
    for i in convert_to_base_5(n):
        s_5 += int(i)       #s_5 là tổng các chữ số của n trong hệ cơ số 5
    v_5 = (n - s_5)/4
    return(v_5)



"""Số số 0 tận cùng của n! chính là v_5_factorial(n) """
print(v_5_factorial(23122003)) #5780496.0
"""Hàm tính số dư của số mới khi chia cho 5"""

def residual_5_new_number(n):
    a = (-1)**(v_5_factorial(n))
    b = [i for i in convert_to_base_5(n)] #tách các chữ số trong hệ cơ số 5 của n
    b.pop(0) # loại bỏ đi phần tù đầu tiên của b do trong công thức thì tích chỉ chạy đến k -1
    for j in b:
        a = a*factorial(int(j))     #tính (a_{0}!).(a_{1}!)...(a_{k-1}!)
    a = a*(2**(4 - v_5_factorial(n)%4))
    return(a%5)

"""Chữ số tận cùng bên phải"""

def last_digit_new_number(n):
    if residual_5_new_number(n)%2 == 0 :    #nếu số mới chia 5 dư 2,4 thì chữ số tận cùng là 2,4
        return(residual_5_new_number(n))
    else:                                   #nếu số mới chia 5 dư 1,3 thì chữ số tận cùng là 6,8
        return(residual_5_new_number(n) + 5)

print(last_digit_new_number(231220039012374927492739412093749224234)) #8.0

