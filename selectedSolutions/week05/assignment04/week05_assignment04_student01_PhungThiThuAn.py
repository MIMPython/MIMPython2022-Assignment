# TH a) Giá cổ phiếu nhận giá trị là một số thực.
import datetime

price = 7.24
i = 0
while price < 58.69:
    price = price*1.07
    i += 1

date = datetime.datetime(2022, 8, 7)
dateEnd = date + datetime.timedelta(days=i)
print(dateEnd, price)

# TH b) Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.
price = 7.24
i = 0
while price < 58.69:
    price = round(price*1.07, 2)
    i += 1

date = datetime.datetime(2022, 8, 7)
dateEnd = date + datetime.timedelta(days=i)
print(dateEnd, price)