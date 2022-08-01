'''
Bài tập 5. (rock-paper-scissors game)
(a) Viết một chương trình để hai người có thể chơi trò chơi kéo - búa - bao với nhau.
(b) Cách tiếp cận đơn giản là cho phép hai người chơi A, B lần lượt đưa ra lựa chọn và nhập nó vào chương trình
thông qua bàn phím (giả sử A nhập trước). 
Cách chơi như vậy không công bằng vì ở mỗi lượt chơi B luôn biết được lựa chọn của A trước khi B đưa ra lựa chọn. 
Thiết kế chương trình để đảm bảo tính công bằng cho trò chơi.
(c) Có thể hiểu tính công bằng theo nghĩa nào khác?
'''

#cau a
#Đặt búa = 0
#   giấy = 1
#   kéo = 2
def func_a(p_1, p_2):
    if (p_1 == p_2):
        print("Hòa")
    elif (p_1 + 1)%3 == p_2:
        print("Người chơi 2 thắng")
    else:
        print("Người chơi 1 thắng")

'''p_1 = int(input("Người chơi 1 nhập: "))
p_2 = int(input("Người chơi 2 nhập: "))
func_a(p_1,p_2)'''

#cau b
from os import system
p_1 = int(input('Nguoi choi 1: '))
system('cls')
p_2 = int(input('Nguoi choi 2: '))
func_a(p_1,p_2)

#cau c
#Công bằng trong chương trình game rock-paper-scissors có thể là mã hóa đầu vào của giá trị của người chơi, 
# ví dụ như người chơi thứ nhất thì đầu vào cộng thêm 13, người chơi thứ 2 đầu vào cộng thêm 7
# một cách khác nữa là ẩn đi giá trị đầu vào
# import getpass
# input_val = getpass.getpass('Password:')