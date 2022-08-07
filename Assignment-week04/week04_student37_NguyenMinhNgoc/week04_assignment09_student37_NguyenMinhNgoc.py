def count_zeros(n):
    if n == 0:
        return 1
    cnt = 0
    for i in range (5, n + 1, 5):
        temp = i
        while temp % 5 == 0: # Đếm số ước 5 của các số chia hết cho 5
            cnt += 1
            temp = temp / 5
    return cnt
print(count_zeros(0))
def last_non_zero_digit(n):
    last_digit = 1
    for i in range (2, n + 1, 1):
        if i % 5 != 0:
            last_digit = (last_digit * (i % 10)) % 10 # Tính chữ số tận cùng của tích cả số nhỏ hơn n không chia hết cho 5
        else:
            temp = i
            while temp % 5 == 0: # Do cứ 1 ước 5 với 1 ước 2 sẽ tạo ra một số 0 nên cứ một ước 5 ta sẽ chia đi một ước 2 so với kết quả trên
                last_digit = last_digit / 2
                temp = temp / 5
            last_digit = (last_digit * (temp % 10)) % 10 # tiếp tục nhân với phần còn lại của số chia hết cho 5
    return int(last_digit)
print(last_non_zero_digit(1000))