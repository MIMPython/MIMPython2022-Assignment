import os
from time import sleep
print("Bài 5: Rock - paper - scissors game")
print()

"""
1: Kéo
2: Búa
3: Bao
"""

def oantuti(A, B):
    if 1 <= A <= 3 and 1 <= B <= 3:
        lst = ["Kéo", "Búa", "Bao"]
        print("A chọn", lst[A-1])
        print("B chọn", lst[B-1])
        print()
        if A > B:
            if A == 3 and B == 1:
                print("Người B thắng cuộc")
                print("A thua cuộc")
            else:
                print("Người A thắng cuộc")
                print("B thua cuộc")
        elif A < B:
            if A == 1 and B == 3:
                print("Người A thắng cuộc")
                print("B thua cuộc")
            else:
                print("Người B thắng cuộc")
                print("A thua cuộc")
        else:
            print("=> A và B đều hòa ván")
    else:
        print("Lỗi game")

#Mở đầu game
print("Chào mừng bạn đến với Rock - paper - scissors game")
sleep(1)        #Chờ 1s vào game
chon = input("Bạn có muốn chơi không? (yes/no) - ")
if chon == "yes":
    while True:
        os.system("cls")        #Xóa terminal
        A = int(input("Người A chọn: "))
        os.system("cls")
        B = int(input("Người B chọn: "))
        os.system("cls")

        oantuti(A, B)
        luachon = input("Bạn có muốn tiếp tục không? (c/k) - ")
        if luachon == "k":
            print("Đã thoát Game")
            break
else:
    print("Đã thoát Game")
