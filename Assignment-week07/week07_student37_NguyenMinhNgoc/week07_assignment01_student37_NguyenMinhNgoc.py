class EmptyList(Exception):
    pass
def list_average(lst):
    try:
        if len(lst) != 0:
            s = sum(lst)/len(lst)
        else:
            raise EmptyList
    except EmptyList as e:
        s = str(type(e)) + ' was raised'
    return s
print(list_average([]))