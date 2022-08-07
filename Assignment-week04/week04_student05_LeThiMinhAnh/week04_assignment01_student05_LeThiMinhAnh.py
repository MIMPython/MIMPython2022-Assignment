
def sortList(lst):
    print(sorted(lst, key=sum))


A = [[1, 2], [3, 0, 4], [2], [4, 5]]
sortList(A)  # [[2], [1, 2], [3, 0, 4], [4, 5]]

# Yêu cầu bổ sung: đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ:
# sắp xếp list này theo thứ tự tăng dần của tích các số trong mỗi list con.


def func(x):
    product = 1
    for i in range(len(x)):
        product *= x[i]
    return product


def sortListbyProduct(lst):
    print(sorted(lst, key=func))


sortListbyProduct(A)  # [[3, 0, 4], [1, 2], [2], [4, 5]]
