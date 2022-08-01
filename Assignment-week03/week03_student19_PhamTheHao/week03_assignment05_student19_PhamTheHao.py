"""
Bài tập 5. (rock-paper-scissors game)
(a) Viết một chương trình để hai người có thể chơi trò chơi kéo - búa - bao với nhau.
(b) Cách tiếp cận đơn giản là cho phép hai người chơi A, B lần lượt đưa ra lựa chọn và nhập 
nó vào chương trình thông qua bàn phím (giả sử A nhập trước). Cách chơi như vậy không công 
bằng vì ở mỗi lượt chơi B luôn biết được lựa chọn của A trước khi B đưa ra lựa chọn. 
Thiết kế chương trình để đảm bảo tính công bằng cho trò chơi.
(c) Có thể hiểu tính công bằng theo nghĩa nào khác?
"""
# a)
a = input("Nguoi thu nhat: ")
b = input("Nguoi thu hai: ")
def rock_paper_scissors(a, b):
    if a == 'r':
        if b == 'r':
            print("Hòa")
        elif b == 'p':
            print('B thắng')
        else:
            print('A thắng')
    elif a == 'p':
        if b == 'p':
            print("Hòa")
        elif b == 's':
            print('B thắng')
        else:
            print('A thắng')
    else:
        if b == 's':
            print("Hòa")
        elif b == 'r':
            print('B thắng')
        else:
            print('A thắng')
rock_paper_scissors(a, b)