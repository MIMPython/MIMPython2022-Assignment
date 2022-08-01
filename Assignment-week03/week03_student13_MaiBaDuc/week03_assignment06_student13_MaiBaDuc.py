'''
Bài tập 6. (probability of coprime integers)
Cho N là một số nguyên dương đủ lớn (N≈106). Lấy ngẫu nhiên hai số nguyên dương từ tập hợp các số nguyên dương không vượt quá N.
Xác suất để hai số này nguyên tố cùng nhau là bao nhiêu? Giá trị này có mối liên quan gì tới số π?
Hãy trả lời những câu hỏi trên bằng cách thực hiện các yêu cầu sau:
(a) Viết một hàm tính ước chung lớn nhất của hai số tự nhiên sử dụng thuật toán Euclid.
(b) Đặt giá trị xác suất cần tìm là P. Tính giá trị của P bằng một trong hai cách:
    Lấy ngẫu nhiên hai số trong tập hợp đã cho rồi kiểm tra tính nguyên tố cùng nhau của chúng.
    Đếm số cặp số nguyên tố cùng nhau trong tất cả cặp số có thể chọn được từ tập số đã cho.
(c) Tìm mối liên hệ giữa giá trị của P và π. Gợi ý: P≈aπb với a,b là hai số dương.
'''
import math
def func_a():
    a = int(input("a: "))
    b = int(input("b: "))
    def func(a,b):
        if a%b==0:
            print(f'uscln(a,b): {b}')
        else:
            c = int(a%b)
            return func(b,c)
    func(a,b)

def func_b():
    n = int(input("N: "))
    def func(a,b):
        if a%b==0:
            return b
        else:
            c = int(a%b)
            return func(b,c)
    count=0 #Tính số cặp nguyên tố cùng nhau trong khoảng tử 1 đến n
    for i in range(1, n+1):
        for j in range(i+1,n+1):
            if func(j,i)==1:
                count += 1
    count_1=0 #Tính số cặp trong khoảng từ 1 đến n
    for i in range(1,n+1):
        for j in range (i+1, n+1):
            count_1 += 1

    p = count/count_1 #Xác suất xuất hiện 2 số nguyên tố cùng nhau trong khoảng từ 1 đến n
    print(math.pi/p)    
