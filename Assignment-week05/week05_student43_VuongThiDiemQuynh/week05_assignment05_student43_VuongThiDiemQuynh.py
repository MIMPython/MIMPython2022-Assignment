'''
Bài tập 5. (infinite loop)
a) Viết một chương trình chạy vô hạn sử dụng vòng lặp while.
b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.
c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary.
'''

# a) Viết một chương trình chạy vô hạn sử dụng vòng lặp while.

while True:
    print("MIM Python")

# b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.

list = [1]
for i in list:
    list.append(i+1)
    print(i,"MIM Python")

# c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary.

def infinity():
    i = 0
    while True:
        yield i 
        i += 1

for n in infinity():
    print(n)
