A = [1,2,3,'a']

def average(list):
    try:
        result = sum(list)/len(list)
        print(f'Average of list: {result}')
    except ZeroDivisionError:
        print("Empty list")
    except TypeError:
        print("The list contains at least one non-numeric element")
average(A)