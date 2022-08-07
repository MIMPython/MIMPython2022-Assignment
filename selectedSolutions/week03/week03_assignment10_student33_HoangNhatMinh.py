"""
    a. bỏ qua những khác biệt về cú pháp của mỗi ngôn ngữ thì cơ bản while trong python tương tự với
    do-while trong C++. điểm khác biệt duy nhất là do-while luôn thực hiện thân vòng lặp 1 lần trước khi
    kiểm tra điều kiện nên trong mọi trường hợp khối do luôn được thực hiện ít nhất 1 lần.

    b. Ta có thể biến đổi tương đương đoạn 2 loại vòng lặp cho nhau chẳng hạn
    C++:
    do {
        action()
    } while (condition)

    Python:
    action()
    while condition:
        action()

    hoặc

    while True:
        action()
        if condition:
            break
"""
