'''
Bài tập 1. (sort a list)
Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử. Cho một list gồm các list con ổn. Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của tổng các số trong mỗi list con.

Ý tưởng: 
    Tính tổng các list con sau đó sắp xếp theo thứ tự tăng dần thành một list mẫu.
    Sau đó dùng vòng lặp for, check tổng của mỗi list con nếu bằng phần tử nào trong list mẫu thì thay đổi vị trí theo phần tử đó.
'''
# Tìm list mẫu
def getSum(list):
    listOfSum = [sum(l) for l in list]
    return sorted(listOfSum)

# Sắp xếp các list con trong một list theo thứ tự tăng dần của tổng 
def getSortedList(list):
    listForm = getSum(list)
    sortedList = []
    for ele in listForm:
        for l in list:
            if ele == sum(l):
                sortedList.append(l)
    return sortedList

print(getSortedList([[1,2], [3,0,4], [2], [4,5]])) #[[2], [1, 2], [3, 0, 4], [4, 5]]



