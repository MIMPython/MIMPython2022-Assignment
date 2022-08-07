def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


# 9a)
def count_num_zero(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n /= 10
    return count


print(count_num_zero(factorial(10)))  # 2


# 9b)
def remove_num_zero(n):
    while n % 10 == 0:
        n /= 10
    return n


num = remove_num_zero(factorial(10))  # 36288.0
print(str(num)[-3: -2]) # 8
