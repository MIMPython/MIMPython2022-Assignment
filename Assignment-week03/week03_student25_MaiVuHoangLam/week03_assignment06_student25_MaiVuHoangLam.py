# 6a)
def greatest_common_divisor(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


print(greatest_common_divisor(8, 12))  # 4


# 6b)
