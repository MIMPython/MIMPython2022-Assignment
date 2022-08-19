'''
Giả sử giá của một cổ phiếu trong một ngày là cố định và phải nằm trong khung từ 93% đến 107% so với giá của ngày liền trước. Biết rằng vào ngày 07/08/2022, giá của cổ phiếu F là 7.24 (đơn vị nghìn đồng). Hỏi thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là khi nào?
Giải Quyết bài tập này trong hai trường hợp sau đây:
a) Giá cổ phiếu nhận giá trị là một số thực.
b) Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.
'''

import datetime

date = datetime.date(2022, 8, 7)

primary = 7.24
day_count = 0
while primary < 58.69:
    primary = primary*1.07
    day_count += 1

new_date = date + datetime.timedelta(days=day_count)
print(f"Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là sau {day_count} ngày kể từ ngày 07/08/2022 tức là ngày {new_date}")

