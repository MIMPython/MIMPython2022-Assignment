# Bài tập 6. (probability of coprime integers)
# Cho N là một số nguyên dương đủ lớn (N≈106). Lấy ngẫu nhiên hai số nguyên dương từ tập hợp
# các số nguyên dương không vượt quá N. Xác suất để hai số này nguyên tố cùng nhau là bao nhiêu?
# Giá trị này có mối liên quan gì tới số π?
# Hãy trả lời những câu hỏi trên bằng cách thực hiện các yêu cầu sau:
# (a) Viết một hàm tính ước chung lớn nhất của hai số tự nhiên sử dụng thuật toán Euclid.
# (b) Đặt giá trị xác suất cần tìm là P. Tính giá trị của P bằng một trong hai cách:

# Lấy ngẫu nhiên hai số trong tập hợp đã cho rồi kiểm tra tính nguyên tố cùng nhau của chúng.
# Đếm số cặp số nguyên tố cùng nhau trong tất cả cặp số có thể chọn được từ tập số đã cho.
# (c) Tìm mối liên hệ giữa giá trị của P và π. Gợi ý: P≈a/π^b với a,b là hai số dương.


def euclid_algo_gcd(num1, num2):
    if num2 == 0:
        return num1
    return euclid_algo_gcd(num2, num1%num2)


if __name__ == '__main__':
    number1 = int(input('Nhập số thứ nhất: '))
    number2 = int(input('Nhập số thứ hai: '))
    gcd_num1_num2 = euclid_algo_gcd(number1, number2)
    print('Ước chung lớn nhất của {} và {} là {}'.format(number1, number2, gcd_num1_num2))