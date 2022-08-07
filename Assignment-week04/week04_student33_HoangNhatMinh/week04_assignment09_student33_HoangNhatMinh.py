# hàm tính factorial để check với thuật toán phía dưới
def factorial(n: int):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


# tìm số chữ số 0 tận cùng của n!
n = 1000
count = 0 # biến đếm số chữ số 0
# nhận xét: do 2! là một số chẵn
# mặt khác 5! = 120, từ 5! trở đi tổng tích lũy của ta luôn có dạng:
#   1 số chẵn nhân với 10^k số 0 tận cùng. (k là số chữ số 0)
#   cho nên sau mỗi lần nhân với một số chia hết cho 5, tổng tích lũy của ta lại tăng lên 1 số 0
#   nhưng cũng có trường hợp tổng tích lũy mới tăng lên 2 chữ số 0 chẳng hạn: (tạm gọi là spec case)
#       24! = 620448401733239439360000
#       25! = 15511210043330985984000000
# ta không cần lưu cả tổng tích lũy trên, chỉ cần lưu một vài giá trị tận cùng trước k số 0
fac = 1
# đây là biến làm điều đó

for i in range(1, n + 1):
    fac *= i
    # để chắc chắn fac sẽ không chứa số 0 tận cùng như trường hợp từ 24! --> 25!
    # ta sử dụng vòng lặp này
    while fac % 10 == 0:
        fac /= 10
        count += 1

    fac %= 10 ** (len(str(i)) + 1)
    # lấy len(str(i)) + 1 chữ số cuối cùng của tổng tích lũy,
    # i càng lớn giá trị fac càng cần lưu trữ nhiều số hơn chẳng hạn
    #   với i = 9, ta cần lưu 3 chữ số (9 * 9 = 81)
    #   với i = 99, ta cần lưu 4 chữ số (99 * 9 = 891)
    # việc tăng kích thước lưu chữ này để chắc chắn rằng dù xảy ra spec case
    # thì ta cũng sẽ không để sót số 0 nào


print(count)    # 249
print(factorial(n))
# thuật toán đúng cho tới n = 1000

# b. chữ số tận cùng bên phải của số được tạo chính là chữ số tận cùng của biến fac mà ta đã lưu
