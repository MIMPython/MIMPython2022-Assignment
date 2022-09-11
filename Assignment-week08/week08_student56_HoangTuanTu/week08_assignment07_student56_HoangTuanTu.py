"""
Xem trong file Ex07.docx
"""
def kCn(k: int, n: int):
    return int(kPn(k, n)/ gt(1, k))


def kPn(k: int, n: int):
    return gt(n, n - k +1)


def gt(start: int, end: int):
    total = end
    for i in range(start, end, -1):
        total *= i
    return total
print("""
a) Xác suất để 1 bộ bài 9 quân ù khan là: {}%
b) Xác suất để 1 bộ bài 10 quân ù khan là: {}%
c) Xác suất để 4 bộ bài tiêu chuẩn ù khan là: {}%
""".format(
kCn(9, 26) / kCn(9, 52) * 100,
kCn(10, 26) / kCn(10, 52) * 100,
kCn(10, 26) * kCn(9, 15) * kCn(9, 15) * kCn(9, 26) / kCn(37, 52), ))
# a) ~ 0,08 %
# b) ~ 0.03 %
# c) ~ 5.932115369544686 * 10^-15 % ~ 0%
