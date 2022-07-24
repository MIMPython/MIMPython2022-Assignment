# Bài tập 5
if __name__ == '__main__':
    listA = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # ở mỗi câu độc lập, sẽ tiến hành thực hiện trên một list là bản sao chép của listA để giữ nguyên trang thái của listA
    # a,  Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
    print("***** Câu a *****")
    listADuplicate = listA[:]
    listADuplicate[3] *= listADuplicate[3]
    print("ListA sau khi thay đổi phần tử 3 là: ")
    print(listADuplicate)
    # [70, 43, 7, 2116, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

    # b, Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau
    # Cách 1: hàm pop
    print("***** Câu b *****")
    listADuplicate = listA[:]
    listADuplicate.pop(3)
    print("ListA sau khi xóa phần tử 3 bằng hàm pop")
    print(listADuplicate)
    # [70, 43, 7, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # Cách 2: hàm delete
    listADuplicate = listA[:]
    del listADuplicate[3]
    print("ListA sau khi xóa phần tử 3 bằng hàm del")
    print(listADuplicate)

    # c,Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.

    listADuplicate = listA[:]
    listADuplicate.append(listADuplicate[-1] ** 2)
    print("***** Câu c *****")
    print("List A sau khi thêm vào cuối list 1 phần tử có giá trị bằng bình phương phần tử cuối")
    print(listADuplicate)

    # d, Tổng số phần tử trong listA:
    print("***** Câu d *****")
    print("Tổng số phần tử trong listA là: " + str(len(listA)))

    # e, Tổng giá trị các phần tử trong listA
    sum = 0
    for i in listA:
        sum += i
    print("***** Câu e *****")
    print("Tổng giá trị phần tử trong listA là: " + str(sum))

    # f, Tổng các phần tử có index 1, 2, 3, 5:
    print("***** Câu f *****")
    sum = listA[1] + listA[2] + listA[3] + listA[5]
    print("Tổng các phần tử có index 1, 2, 3, 5 là:" + str(sum))

    # g, Tạo ra một list mới mà các phần tử có thứ tự đảo ngược từ listA cũ bằng 2 cách:
    # Cách 1: hàm reverse
    print("***** Câu g *****")
    newList = listA[:]
    newList.reverse()
    print("Reverse by reverse(): ", newList)
    # Cách 2: dùng vòng for để thêm cách phần tử của listA và list mới
    newList = []
    sizeList = len(listA)
    for i in reversed(range(0, sizeList)):
        newList.append(listA[i])
    print("Reverse by loop: ", newList)

    # h, tách list ban đầu thành 2 list con, một list chẵn, một list lẻ
    print("***** Câu h *****")
    evenList = []
    oddList = []
    for i in range(0, sizeList, 1):
        if listA[i] % 2 == 0:
            evenList.append(listA[i])
        else:
            oddList.append(listA[i])

    print("ListA: ", listA)
    print("even list: ", evenList)
    print("odd list: ", oddList)

    # i, tạo listB từ List A sao cho list B là các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải
    print("***** Câu i *****")
    listB = listA[:]
    listB.sort(reverse=True)
    print(listB)

    # j, So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
    print("***** Câu j *****")
    print("List A và List B có độ dài bằng nhau: True or False ?")
    print(len(listA) == len(listB))

    # k , ghép list A và list B thành List C
    print("***** Câu k *****")
    listC = listA + listB
    print("ListC: ", listC)
