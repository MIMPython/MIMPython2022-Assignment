# Tìm thừa số nguyên tố lớn nhất
number = 600851475143
primeFactor = 2
while number != 1:
    if number % primeFactor == 0:
        number = number / primeFactor
        # thao tác này sẽ lặp lại cho đến khi primeFactor không còn là prime factor của number nữa
    else:
        primeFactor = primeFactor + 1
        # primeFactor cuối cùng luôn luôn là prime factor lớn nhất
print(primeFactor)          # 6857
