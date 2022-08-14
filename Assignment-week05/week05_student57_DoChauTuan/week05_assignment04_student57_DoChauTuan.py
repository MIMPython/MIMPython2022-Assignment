# 4

# a
import random
F_original = 7.24
day = 0
while F_original < 58.69:
    interest_rate = random.uniform(0.93, 1.07)
    F_original *= interest_rate
    day += 1
print(day)

# b
F_first = 7.24
day = 0
while F_first < 58.69:
    interest_rate = random.uniform(0.93, 1.07)
    F_first *= interest_rate
    F_first = round(F_first, 2)
    day += 1
print(day)