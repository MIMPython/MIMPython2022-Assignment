"""
Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử.
Cho một list gồm các list con ổn.
Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của tổng các số trong mỗi list con.
"""
import numpy as np


def isStableList(lst: list) -> bool:
    """
    Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử.
    """
    if lst:
        for i in lst:
            if isinstance(i, float):
                return False
        return True
    else:
        return False


def compareStableList(l1: list, l2: list) -> None:
    """
    so sánh 2 stable list
    nếu list nào có tổng lớn hơn -> list đó lớn hơn
    nếu list nào có tổng bằng nhau -> so sánh độ lệch chuẩn
    :param l1: list đầu vào thứ nhất
    :param l2: list đầu vào thứ hai
    :return: true nếu l1 lớn hơn l2 theo logic so sánh và ngược lại
    """
    if isStableList(l1) and isStableList(l2):
        s1 = sum(l1)
        s2 = sum(l2)
        if s1 == s2:
            std1 = np.std(l1)
            std2 = np.std(l2)
            return std1 < std2
        else:
            return s1 > s2
    else:
        return None


stableList = [[1, 2, 3, 4], [1], [1, 2, 3], [1, 2], [1, 2, 2, 5]]
for i in range(5):
    for j in range(i + 1, 5):
        if compareStableList(stableList[i], stableList[j]):
            tmp = stableList[i]
            stableList[i] = stableList[j]
            stableList[j] = tmp

print(stableList)
