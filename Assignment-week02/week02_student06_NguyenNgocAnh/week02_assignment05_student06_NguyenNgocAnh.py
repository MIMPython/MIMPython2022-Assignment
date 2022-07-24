# (a) Thay giá trị tại vị trí thứ position của list A bởi
# bình phương của chính giá trị đó.
def change_value_by_square(values, position):
    values[position - 1] **= 2
    print(values)


# (b) Xóa phần tử thứ position của list A bằng ít
# nhất hai cách khác nhau (Cách 1)
def delete_position_1(values, position):
    values.pop(position-1)
    print(values)


# (b) Xóa phần tử thứ 3 của list A bằng ít
# nhất hai cách khác nhau (Cách 2)
def delete_position_2(values, position):
    values1 = []
    for i in range(len(values)):
        if i == position - 1:
            continue
        values1.append(values[i])
    return values1


# (c) Thêm vào phía cuối list A một phần tử có giá trị
# bằng với bình phương của phần tử cuối cùng của list A.
def add_element_at_end(values):
    if len(values) != 0:
        values.append(values[len(values)-1]**2)
        print(values)


# (d) Tính số phần tử trong list.
def number_of_elements(values):
    print('Number of elements:')
    print(len(values))


# (e) Tính tổng các phần tử trong list.
def sum_of_elements(values):
    res = 0
    for value in values:
        res += value
    print('Sum:')
    print(res)


# (f) Tính tổng của các phần tử có
# chỉ số (index) 1, 2, 3, 5 trong list.
def sum_of_index(values, indexs):
    res = 0
    for index in indexs:
        res += values[index]
    print('Sum of:')
    print(indexs)
    print(res)


# (g) Tạo ra một list mới có thứ tự các phần tử đảo
# ngược với một list đã cho
# (bằng ít nhất hai cách khác nhau).
# Cách 1
def reverse_list_1(values):
    values1 = values.copy()
    values1.reverse()
    return values1


# (g) Tạo ra một list mới có thứ tự các phần tử đảo
# ngược với một list đã cho
# (bằng ít nhất hai cách khác nhau).
# Cách 2
def reverse_list_2(values):
    values1 = []
    for i in range(len(values)):
        values1.append(values[len(values)-1-i])
    return values1


# (h) Tách list ban đầu thành hai list,
# một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
def odd_list_even_list(values, odds, evens):
    for value in values:
        if value % 2 == 1:
            odds.append(value)
        else:
            evens.append(value)


# (i) Tạo một list B gồm các phần tử của list A
# được sắp xếp theo thứ tự giảm dần từ trái qua phải.
def de_sort(values):
    values1 = values.copy()
    values1.sort()
    values1.reverse()
    return values1


# (k) Ghép hai list A và list B lại với
# nhau thành list C.
def extend_list(values1, values2):
    values = values1.copy()
    values.extend(values2)
    return values


if __name__ == '__main__':

    # khởi tạo A
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    print('A ban đầu:')
    print(A)

    print('(a) Thay giá trị tại vị trí thứ 3 của list A bởi '
          'bình phương của chính giá trị đó.')
    change_value_by_square(A, 3)

    print('(b) Xóa phần tử thứ 3 của list A')
    delete_position_1(A, 3)

    print('(c) Thêm vào phía cuối list A một phần tử có giá trị '
          'bằng với bình phương của phần tử cuối cùng của list A.')
    add_element_at_end(A)

    print('(d) Tính số phần tử trong list.')
    number_of_elements(A)

    print('(e) Tính tổng các phần tử trong list.')
    sum_of_elements(A)

    print('(f) Tính tổng của các phần tử '
          'có chỉ số (index) 1, 2, 3, 5 trong list.')
    sum_of_index(A, [1, 2, 3, 5])

    print('(g) Tạo ra một list mới có thứ tự '
          'các phần tử đảo ngược với một list đã cho')
    reA = reverse_list_1(A)
    print(reA)

    print('(h) Tách list ban đầu thành hai list, '
          'một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.')
    odd_list = []
    even_list = []
    odd_list_even_list(A, odd_list, even_list)
    print('Chẵn: ')
    print(even_list)
    print('Lẻ: ')
    print(odd_list)

    print('(i) Tạo một list B gồm các phần tử của list A '
          'được sắp xếp theo thứ tự giảm dần từ trái qua phải.')
    B = de_sort(A)
    print('B: ')
    print(B)

    print('So sánh độ dài của hai list A và list B, bằng True, khác False: ')
    print(len(A) == len(B))

    print('(k) Ghép hai list A và list B lại với nhau thành list C.')
    C = extend_list(A, B)
    print(C)
