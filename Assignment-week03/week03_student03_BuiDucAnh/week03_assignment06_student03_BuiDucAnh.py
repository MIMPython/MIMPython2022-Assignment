# a) Tìm ước số chung lớn nhất

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

if __name__ == "__main__":
    print(greatest_common_divisor(64, 72)) #8
    print(greatest_common_divisor(197, 0)) #197

# b)Tính xác suất lấy được 2 số nguyên tố cùng nhau trong 1 tập cho trước
 
# Giả sử tập có N = 10 ^6 phần tử  
N = 10**6

# Tính giai thừa của n
def factorial (n):
    result = 1
    if n == 0 or n == 1:
        return result
    else:
        for i in range(2, n+1):
            result *= i
        return result

# Tính số trường hợp lấy ngẫu nhiên 2 phần tử trong N phần tử
randomTwoElements = (factorial(N))/(factorial(2)*factorial(N-2))
print(randomTwoElements)

# Tính số cặp nguyên tố cùng nhau trong tập N phần tử
# Lấy ngẫu nhiên 2 số không kể thứ tự
# Nếu 1 trong 2 số là số 1
case_1 = N - 1

# 2 số ngẫu nhiên không có số 1 
case_2 = 0
for i in range(2, N+1):
    for j in range(i, N):
        if greatest_common_divisor(i, j+1) == 1:
            case_2 += 1

# Xác suất lấy ngẫu nhiên 2 số đi rừng là:
P = (case_1 + case_2)/randomTwoElements
print(P)