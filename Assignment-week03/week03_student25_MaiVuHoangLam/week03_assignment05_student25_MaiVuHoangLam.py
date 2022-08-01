import os

# 5a)
player_1 = input("Enter your choice (rock, paper, scissor): ")

player_2 = input("Enter your choice (rock, paper, scissor): ")


def game(x, y):
    if x == y:
        print("Tie")
    elif x == "rock":
        if y == "scissor":
            print("Player 1 win")
        elif y == "paper":
            print("Player 2 win")
    elif x == "scissor":
        if y == "rock":
            print("Player 2 win")
        elif y == "paper":
            print("Player 1 win")
    elif x == "paper":
        if y == "scissor":
            print("Player 2 win")
        elif y == "rock":
            print("Player 1 win")


game(player_1, player_2)

# 5b) Chỉ cần thêm lệnh "os.system('cls')" sau khi player 1 nhập input

# 5c) Tính công bằng là khi mọi người không thấy bị thua thiệt so với người khác
