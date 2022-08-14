# bai tap 4
# Giá cổ phiếu hôm nay nằm trong khoảng 93% đến 107% giá cổ phiếu ngày hôm trước
# giá cổ phiếu ban đầu là: 7.24 nghìn, giá cổ phiếu kỳ vọng là 58.69 nghìn
# Thời điểm sớm nhất nếu có thể xảy ra khi tất cả các ngày giá trị cổ phiếu hôm trước đều = 107 của ngày hôm sau

if __name__ == '__main__':
    price = 7.24
    expectPrice = 58.69
    day = 0
    while price < expectPrice:
        price = 1.07 * price
        day = day + 1
    # float
    print(price)
    # float with 2 number behind point

    print(f"{price:.2f}")
    print(day)
