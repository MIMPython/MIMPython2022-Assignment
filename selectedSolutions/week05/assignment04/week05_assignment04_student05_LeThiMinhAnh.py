# a) Giá cổ phiếu nhận giá trị là một số thực.

from datetime import timedelta
from datetime import date


def veBoKhongKho(startValue, endValue, startDate):
    startDate = date.fromisoformat(startDate)
    count = 0
    while not(startValue*(100/107) <= endValue and startValue >= endValue):
        startValue *= 1.07
        count += 1
    endDate = startDate + timedelta(days=count)
    print(
        f"Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc {endValue} nghìn đồng là:", endDate)


veBoKhongKho(7.24, 58.69, "2022-08-07")
# Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là: 2022-09-07

# b) Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.


def veBoKhongKho_2(startValue, endValue, startDate):
    startDate = date.fromisoformat(startDate)
    count = 0
    while not(startValue*(100/107) <= endValue and startValue >= endValue):
        startValue = float('%.2f' % (startValue*1.07))
        count += 1
    endDate = startDate + timedelta(days=count)
    print(
        f"Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc {endValue} nghìn đồng là:", endDate)


veBoKhongKho_2(7.24, 58.69, "2022-08-07")
# Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là: 2022-09-07
