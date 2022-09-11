num = 0
maxlength = 0
for i in range(2, 1000001):
    cnt = 1
    temp = i
    while temp != 1:
        if temp % 2 == 0:
            temp = temp / 2
        else:
            temp = 3 * temp + 1
        cnt += 1
    if cnt > maxlength:
        maxlength = cnt
        num = i
print('The starting number ' + str(num) + ' produces a sequence of ' + str(maxlength))