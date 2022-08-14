"""
a) Viết một chương trình chạy vô hạn sử dụng vòng lặp while.
    while 1: 2
b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.
    for i in (1, 2):
        i -= 1
c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary.
class abcdef:
    def __iter__(self):
        return self

    def __next__(self):
        return self

for i in abcdef():
    print("vo han chua?")
"""


