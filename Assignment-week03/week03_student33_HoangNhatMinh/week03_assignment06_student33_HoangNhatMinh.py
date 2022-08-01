# a. GCD by Euclid algorithm
import itertools
import math
import random


def GCD(a: int, b: int):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


print(GCD(16, 32))  # 16
print(GCD(32, 16))  # 16
print(GCD(0, 12))   # 12


# b.
# cách 1
N = 1000
coprime = 0
total = 0
for combi in itertools.combinations(list(range(1, N)), 2):
    if math.gcd(combi[0], combi[1]) == 1:
        coprime = coprime + 1
    total = total + 1
P = coprime/total
print(P)    # 0.6094090082066034

# Cách 2
coprime = 0
total = 0
while True:
    total = total + 1
    ran1 = random.randint(1, 10 ** 6)
    ran2 = random.randint(1, 10 ** 6)
    if math.gcd(ran1, ran2) == 1:
        if coprime < 50:
            coprime = coprime + 1
        else:
            break
print(coprime/total)    # 0.6944444444444444

# Kết quả có độ chính xác nhất
print(6/(math.pi**2))   # 0.6079271018540267

# c. dạng tổng quát của biểu thức liên hệ giữa P và pi là aP^b = Pi hoặc P = aPi^b do P và Pi đều là 2 hệ số tự do
#    ta sử dụng 1 trong 2 dạng và mò giá trị (a,b) trong khoảng nhất định
#    do P và Pi dương nên ta chọn a có khoảng (0,10] b có khoảng [-10,10]
A = [round(0.3*i, 1) for i in range(1, 30)]
B = [round(-4 + i * 0.2, 1) for i in range(1, 30)]
cases = []
minValue = 0.005
a = 0
b = 0
for i in itertools.product(A, B):
    tmp = abs(P - i[0] * math.pi ** i[1])     # P = aPi^b
    if tmp < 0.005:                           # 0.005 là giá trị epsilon
        if minValue > tmp:
            minValue = tmp
            a = i[0]
            b = i[1]

print(a, ' ', b)    # 6.0   -2.0     # vậy hệ thức liên hệ giữa P và pi là P = 6*pi^-2