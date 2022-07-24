from xml.dom.minidom import Element


if __name__ == '__main__':
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
    A[2]*= A[2]
    print(A)
# (b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
#   Dùng pop: 
    A.pop(2)
    print(A)
#   Dùng delete:
    del A[2]
    print(A)
# (c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
    LastElement = A[len(A)-1]
    A.append(LastElement**2)
    print(A)
# (d) Tính số phần tử trong list.
    NumberOfElement = len(A)
    print(NumberOfElement)
# (e) Tính tổng các phần tử trong list.
    SumOfElement = 0
    for Element in A:
        SumOfElement+=Element
    print(SumOfElement)
# (f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
    SumOfElementIndex= A[1] + A[2] + A[3] + A[4] + A[5]
# (g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
#     Cách 1:
    FirstList = []
    for Element in A:
        FirstList.append(Element)
    FirstList.reverse()
    print(FirstList)
# Cách 2:
    SecondList = []
    for index in range(1, len(A) + 1):
        SecondList.append(A[-index])
    print(SecondList)
# (h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
    EvenNumberList = []
    OddNumberList = []
    for element in A:
        if element % 2 == 0:
            EvenNumberList.append(element)
        else:
            OddNumberList.append(element)
    print(EvenNumberList)
    print(OddNumberList)
# (i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
    B = []
    for element in A:
        B.append(element)
    B.sort()
    B.reverse()
    print(B)
# (j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
    print("len(A) == len(B) ?", len(A) == len(B))
# (k) Ghép hai list A và list B lại với nhau thành list C.
    C = A + B
    print(C)