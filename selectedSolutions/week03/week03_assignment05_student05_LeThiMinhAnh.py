# a) Viết một chương trình để hai người có thể chơi trò chơi kéo - búa - bao với nhau.
import getpass
from random import randint


def main():
    player_A, player_B = sym()
    rock_paper_scissors_game(player_A, player_B)


def sym():
    count = randint(0, 10)
    if count % 2 == 0:
        player_A = getpass.getpass(
            "Player A, do you want to be rock, paper or scissors? ")
        player_B = getpass.getpass(
            "Player B, do you want to be rock, paper or scissors? ")
    else:
        player_B = getpass.getpass(
            "Player B, do you want to be rock, paper or scissors? ")
        player_A = getpass.getpass(
            "Player A, do you want to be rock, paper or scissors? ")
    input("Press enter to continue.")
    print("\n")
    print(f"Player A, you are {player_A}.")
    print(f"Player B, you are {player_B}.")
    return (player_A, player_B)


def rock_paper_scissors_game(player_A, player_B):
    if player_A == player_B:
        print("There is a tie.")
    elif player_A == "rock":
        if player_B == "paper":
            print("Congratulations, Player B, you won!")
        else:
            print("Congratulations, Player A, you won!")
    elif player_A == "paper":
        if player_B == "scissors":
            print("Congratulations, Player B, you won!")
        else:
            print("Congratulations, Player A, you won!")
    elif player_A == "scissors":
        if player_B == "rock":
            print("Congratulations, Player B, you won!")
        else:
            print("Congratulations, Player A, you won!")


main()

# c) Có thể hiểu tính công bằng theo nghĩa nào khác?
# Hai người chơi A, B đều có cơ hội được nhập lựa chọn trước.
