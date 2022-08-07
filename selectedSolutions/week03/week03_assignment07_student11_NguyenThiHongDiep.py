# Hàm kiểm tra số nguyên tố
def isPrimeNumber(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

# Hàm phân tích số
def numberAnalysis(n):
    result = []
    i = 2
    while (n > 1):
        if (isPrimeNumber(i)):
            if (n % i == 0):
                result.append(i)
                n = n / i
            else:
                i = i + 1
        else:
            i = i + 1
    return result       

A = numberAnalysis(600851475143)
print(A) # [71, 839, 1471, 6857]
print(max(A)) # 6857

        