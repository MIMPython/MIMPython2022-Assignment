# Bài tập 5. Cho list A với các giá trị dưới đây
if __name__ == "__main__":
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
    A[2] = A[2]**2
    print(A) # [70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # (b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
    # Cách 1: Sử dụng pop
    A.pop(2)
    print(A) # [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # Cách 2: Sử dụng del
    del A[2]
    print(A) # [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    # (c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
    A.append(A[-1]**2)
    print(A) # [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
    # (d) Tính số phần tử trong list.
    print(len(A)) # 14
    # (e) Tính tổng các phần tử trong list.
    print(sum(A)) # 3315
    # (f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
    print(sum(A[1:4]) + A[5]) # 189
    # (g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
    # Cách 1: Sử dụng reverse
    A_copy = A.copy()
    A_copy.reverse()
    print(A_copy) # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]
    # Cách 2: Sử dụng list comprehension
    A_imitated = [A[len(A) - i - 1] for i in range(len(A))]
    print(A_imitated) # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]
    # (h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
    even_list = [A[i] for i in range(len(A)) if A[i] % 2 == 0]
    odd_list = [A[i] for i in range(len(A)) if A[i] % 2 == 1]
    print(even_list) # [70, 34, 80]
    print(odd_list)  # [43, 77, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
    # (i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
    B = A.copy()
    B.sort()
    print(B) # [1, 3, 3, 5, 34, 35, 43, 49, 53, 53, 70, 77, 80, 2809]
    # (j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
    print(len(A) == len(B)) # True
    # (k) Ghép hai list A và list B lại với nhau thành list C.
    C = A.copy()
    C.extend(B)
    print(C) # [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809, 1, 3, 3, 5, 34, 35, 43, 49, 53, 53, 70, 77, 80, 2809]




