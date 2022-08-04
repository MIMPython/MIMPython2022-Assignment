def infinite_loop():
    sum = 1
    while True:
        sum += 1
        print(sum)


if __name__ == '__main__':
    infinite_loop()