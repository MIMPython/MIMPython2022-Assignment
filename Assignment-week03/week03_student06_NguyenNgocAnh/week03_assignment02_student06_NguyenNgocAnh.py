def large_sum():
    sum = 0
    for i in range(100):
        number = int(input())
        sum += number
    str_sum = str(sum)
    result = ''
    for i in range(10):
        result += str_sum[i]
    return result


if __name__ == '__main__':
    print(large_sum())
