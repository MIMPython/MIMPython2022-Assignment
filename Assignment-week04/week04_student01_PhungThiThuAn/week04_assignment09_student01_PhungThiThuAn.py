from math import factorial

def countRight0InFactorial(n):
    factorialInStr = str(factorial(n))
    count = 0
    for i in reversed(factorialInStr):
        if i == '0':
            count += 1
        else:
            break
    return f'{n}! = {factorial(n)}.\nSố chữ số 0 ở tận cùng bên phải là: {count}.\nChữ số tận cùng bên phải mới là: {i}.'

print(countRight0InFactorial(19))
# 19! = 121645100408832000.
# Số chữ số 0 ở tận cùng bên phải là: 3.
# Chữ số tận cùng bên phải mới là: 2.