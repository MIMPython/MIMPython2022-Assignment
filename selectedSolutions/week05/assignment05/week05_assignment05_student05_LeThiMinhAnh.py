# a) Viết một chương trình chạy vô hạn sử dụng vòng lặp while.
while 1:
    1
# b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.
numberList = [0]
for i in numberList:
    numberList.append(i+1)
    print(i)
# c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary
import itertools
for i in itertools.repeat(0):
    print(i)
