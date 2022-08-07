def factorial_num(num):
    k = 5
    count = 0
    while num / k >= 1:
        count += int(num / k)
        k *= 5
    return count


def find_last_digit(num):
    mul = 1
    for i in range(1, num + 1):
        mul *= i
        while mul % 10 == 0:
            mul /= 10
        mul = mul % 1000
    return mul % 10


if __name__ == '__main__':
    n = int(input())
    print(factorial_num(n))
    print(find_last_digit(n))
