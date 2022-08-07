# Bai 9

# a)
def zero_right(n):
    res = n // 5
    i = 2
    while 5 ** i <= n:
      res += i - 1
      i += 1

    return res


if __name__ == "__main__":
    print(zero_right(4))
    print(zero_right(5)) # 1
    print(zero_right(25)) # 6