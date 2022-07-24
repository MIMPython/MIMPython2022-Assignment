# (1) Half Pyramid
def half_pyr(n):
    for i in range(n+1):
        res = ''
        for j in range(i):
            res += '*'
        print(res)


# (2) Inverted Half Pyramid
def in_half_py(n):
    n1 = n
    while n1 > 0:
        res = ''
        for i in range(n1):
            res += '*'
        n1 = n1 - 1
        print(res)


# (3) Hollow Inverted Half Pyramid
def hollow_in_half_py(n):
    n1 = n
    first_line = ''
    for i in range(n1):
        first_line += '*'
    print(first_line)
    n1 = n1 - 1
    while n1 > 0:
        res = ''
        for i in range(n1):
            if i == 0 or i == n1 - 1:
                res += '*'
            else:
                res += ' '
        n1 = n1 - 1
        print(res)


# (4) Full Pyramid
def full_py(n):
    n1 = n*2
    for i in range(n):
        res = ''
        for j in range(n1):
            if j < n-i - 1 or j > n + i :
                res += ' '
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        res += '*'
                    else:
                        res += ' '
                else:
                    if j % 2 == 0:
                        res += ' '
                    else:
                        res += '*'
        print(res)


# (5) Inverted Full Pyramid
def in_full_py(n):
    n1 = n * 2
    i = n
    while i > 0:
        res = ''
        for j in range(n1):
            if j < n - i or j > n + i - 1:
                res += ' '
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        res += '*'
                    else:
                        res += ' '
                else:
                    if j % 2 == 0:
                        res += ' '
                    else:
                        res += '*'
        print(res)
        i = i - 1


# (6) Hollow Full Pyramid
def hol_full_py(n):
    n1 = n * 2
    last_line = ''
    for i in range(n):
        last_line += ' *'
    for i in range(n-1):
        res = ''
        for j in range(n1):
            if j == n  - i or j == n + i:
                res += '*'
            else:
                res += ' '
        print(res)
    print(last_line)


if __name__ == '__main__':
    print('(1) Half Pyramid')
    half_pyr(6)
    print('(2) Inverted Half Pyramid')
    in_half_py(6)
    print('(3) Hollow Inverted Half Pyramid')
    hollow_in_half_py(6)
    print('(4) Full Pyramid')
    full_py(6)
    print('(5) Inverted Full Pyramid')
    in_full_py(6)
    print('(6) Hollow Full Pyramid')
    hol_full_py(6)
