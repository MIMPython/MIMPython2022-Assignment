# Bài tập 4. (Fibonacci numbers)
# Dãy số Fibonacci {Fn}∞n=0 được định nghĩa bằng công thức truy hồi:
#
# F0=0,F1=1
# Fn+2=Fn+1+Fn∀n≥0
# Viết một chương trình tính số Fibonacci Fn với một số tự nhiên n cho trước.
# Hãy giải quyết bài tập này bằng nhiều cách khác nhau,
# trong đó có cách sử dụng thư viện numpy, sympy.

import numpy as np


def fibonacci_recursive(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_numpy(n):
    # a = (1 + sqrt(5)) / 2
    # b = (1 - sqrt(5)) / 2
    # Fn = (a^n - b^n) / sqrt(5)
    sqrt_5 = np.sqrt(5)
    a = (1 + sqrt_5) / 2
    b = (1 - sqrt_5) / 2
    Fn = (a**n - b**n) / sqrt_5
    return int(Fn)


if __name__ == '__main__':
    n =int(input('Nhập n: '))
    print(str(fibonacci_recursive(n)))
    print(fibonacci_numpy(n))
