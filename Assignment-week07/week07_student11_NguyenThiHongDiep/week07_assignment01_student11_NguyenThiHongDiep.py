def ListAverage(list, digits = 1):
    try:
        sum = 0
        for i in list:
            sum = sum + i
        average = round(sum / len(list), digits)
        return f'Average: {average}'
    except ZeroDivisionError:
        return 'Your list is empty.'
    except TypeError:
        return 'Your list has a invalid type element.'

A = []
print(ListAverage(A)) # Your list is empty.

B = ['d', 3]
print(ListAverage(B)) # Your list has a invalid type element.

C = [23.6, 15.1, 1.0, 6.2, 10.1, 12]
print(ListAverage(C)) # Average: 11.3

D = [3.678, 1.123, 17.01234, 6.28, 10.1, 12]
print(ListAverage(D, 3)) # Average: 8.366

