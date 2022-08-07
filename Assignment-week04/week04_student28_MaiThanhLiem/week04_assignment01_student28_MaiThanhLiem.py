# Main part of exercise
def reasonabilityOfList(A):
    if type(A) != list:
        return 0
    if len(A) < 1:
        return 0
    for element in A:
        if type(element) != int and type(element) != float:
            return 0
    return 1


def sortBySum(A: list):
    for element in A:
        if reasonabilityOfList(element) == 0:
            B = "Elements in list are not reasonable sub-lists, can't do the sorting."
            return B
    B = sorted(A, key=lambda list: sum(list))
    return B


A0 = [[1, 2, 3, 4], []]
A1 = ["1, 2", "3, 4"]
A2 = [1, 2, 3, 4]
A = [[1, 2], [3, 0, 4], [2], [4, 5]]
print(sortBySum(A0))
print(sortBySum(A1))
print(sortBySum(A2))
print(sortBySum(A))

# Bonus part
"""
Another criterion to compare two reasonable list is by the length of the list.
"""


def bonusSorting(A: list):
    for element in A:
        if reasonabilityOfList(element) == 0:
            B = "Elements in list are not reasonable sub-lists, can't do the sorting."
            return B
    B = sorted(A, key=lambda list: sum(list) and len(list))
    return B


print(bonusSorting(A))
