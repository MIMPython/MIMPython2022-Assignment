def average(list, digits=1):
    '''
    list: input list to calculate average
    diAfCom: The number of decimals to use when rounding the number. Default is 1

    '''
    try:
        sum = 0
        for i in list:
            sum += i
        result = round(sum/len(list), digits)
        return f'average:{result}'
    except ZeroDivisionError:
        return 'Your list is empty.'
    except TypeError:
        return 'Your list has a invalid type element.'

a = []
print(a, average(a))
b = [7, 5, 't', 4, 6]
print(b, average(b))
c = [1.99, 3.9, 5.7, 2, 9]
print(c, average(c))
print(c, average(c, 3))

'''
Output:
[] Your list is empty.
[7, 5, 't', 4, 6] Your list has a invalid type element.
[1.99, 3.9, 5.7, 2, 9] average:4.5
[1.99, 3.9, 5.7, 2, 9] average:4.518

'''