""" a) Viết một chương trình chạy vô hạn sử dụng vòng lặp while.
-> Trả lời:"""
def infiiteLoopWithWhile():
    while 1: 1

""" b) Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.
-> Trả lời:"""
def infiiteLoopWithFor():
    loop = [0]
    for _ in loop: loop.append(1)

""" c) Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in)
không phải là một list, tuple, set, hay dictionary
-> Trả lời:."""
def infiiteLoop():
    for i in iter(int, 1): print(i)
infiiteLoop()