import math

# a
def greatest_common_divisor(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        while a % b != 0:
            temp = a % b
            a = b
            b = temp
        return b
    elif a < b:
        while b % a != 0:
            temp = b % a
            b = a
            a = temp
        return a
    else:
        return b


print(greatest_common_divisor(27, 8))

# b
n = 10**6
count = 0
for i in range(n):
    for j in range(n):
        if greatest_common_divisor(i + 1, j + 1) == 1:
            count += 1
p = count / (n**2)
print(p)

# c
# solve Diophantine equation
for a in range(100):
    for b in range(100):
        error = (a / (math.pi**b)) - p
        # try pairs of integers and evaluate the error between p and the function
        error = abs(error)
        if error < (1 / (10**3)):
            print(a, b)
            break
