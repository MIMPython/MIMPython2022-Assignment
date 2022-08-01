"""
Bài tập 6. (probability of coprime integers)
"""
# (a) Viết một hàm tính ước chung lớn nhất của hai số tự nhiên sử dụng thuật toán Euclid.
def gcd(a, b):
    if a == 0 :
        return b
    elif b == 0:
        return a
    elif a < b:
        return gcd(b % a, a)
    else:
        return gcd(a % b, b)

print(gcd(6, 8)) # gcd(6,8) = 2
print(gcd(21, 28)) # gcd(21, 28) = 7
# (b) Đặt giá trị xác suất cần tìm là P. Tính giá trị của P bằng một trong hai cách:

count = 0
for a, b in range(n):
    if gcd(a, b) == 1:
        count += 1
prob = count