# a. Giá cổ phiếu nhận giá trị là một số thực.
stockPrice = 7.24
days = 0
while (stockPrice < 58.69):
    stockPrice = stockPrice*1.07
    days += 1
print('Sau', days, 'ngay thi gia cua co phieu nay cham moc 58.69 nghin dong va gia cua co phieu la', stockPrice, 'nghin dong.')
# Sau 31 ngay thi gia cua co phieu nay cham moc 58.69 nghin dong va gia cua co phieu la 58.97061736449431 nghin dong.

# b. Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.
stockPrice = 7.24
days = 0
while (stockPrice < 58.69):
    stockPrice = round(stockPrice*1.07, 2)
    days += 1
print('Sau', days, 'ngay thi gia cua co phieu nay cham moc 58.69 nghin dong va gia cua co phieu la', stockPrice, 'nghin dong.')
# Sau 31 ngay thi gia cua co phieu nay cham moc 58.69 nghin dong va gia cua co phieu la 58.95 nghin dong.