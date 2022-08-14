# a)Viết 1 chương trình chạy vô hạn sử dụng vòng lặp while
def infinite_while():
    while True:
        print("Hello.")

# b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.
def infinite_for():
    list_number = [1,2]
    for i in list_number:
        list_number.append(i + 1)
        print("Hello.")
infinite_for()

# c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối 
# tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary

