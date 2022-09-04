#  exersise 1: make function: input: list, output: avarage of list
import numpy as np


def getMeanList(list):
    try:
        if len(list) == 0:
            raise Exception("empty list")  # exception empty list
        for element in list:
            isNumber = type(element) is float or type(
                element) is int  # exception element not a number
            if not isNumber:
                raise TypeError()

        array = np.array(list, dtype=float)
        return np.mean(array)
    except TypeError:
        print("element in list is not a number")
    except Exception:
        print("list is empty")


if __name__ == '__main__':
    list1 = [2, 3, 4, 1]
    print(getMeanList(list1))  # 2.5
    list2 = []
    print(getMeanList(list2))  # list is empty
    list3 = [2, 'a']
    print(getMeanList(list3))  # element in list is not a number
