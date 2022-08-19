#  bai tap 7
#  số chính phương: là số mà có căn bậc 2 là số tự nhiên ví dụ: 1, 4, 9, ...
#  Số palindrome: số mà nếu viết xuôi hay viết ngược đều cùng giá trị
from math import sqrt


def isSquareNumber(number):
    endNumber = round(sqrt(number) + 1)
    for i in range(1, endNumber):
        if i * i == number:
            return True

    return False


def isPalidromeNumber(number):
    number = str(number)
    reverseNumber = number[::-1]
    if number == reverseNumber:
        return True
    else:
        return False


if __name__ == '__main__':
    number = 1
    while True:

        while isPalidromeNumber(number) and isSquareNumber(number):
            print(number)
            number = number + 1
        number = number + 1

# result
# 1
# 4
# 9
# 121
# 484
# 676
# 10201
# 12321
# 14641
# 40804
# 44944
# 69696
# 94249
# 698896
# 1002001
# 1234321
# 4008004
# 5221225
# 6948496
