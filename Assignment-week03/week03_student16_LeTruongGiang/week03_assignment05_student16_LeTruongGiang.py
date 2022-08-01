import getpass

p1_call = getpass.getpass("Player 1, Enter rock/paper/scissors: ")
p2_call = getpass.getpass("Player 2, Enter rock/paper/scissors: ")

def rock_paper_scissors(player_1, player_2):
    a_list = ["rock", "paper", "scissors"]

    while player_1 not in a_list or player_2 not in a_list:
        print ("Invalid input. Please give a valid input.")
        player_1 = getpass.getpass("Player 1, Enter rock/paper/scissors: ")
        player_2 = getpass.getpass("Player 2, Enter rock/paper/scissors: ")

    while player_1 == player_2:
        print( "Nobody wins. Try again")
        player_1 = getpass.getpass("Player 1, Enter rock/paper/scissors: ")
        player_2 = getpass.getpass("Player 2, Enter rock/paper/scissors: ")

    if player_1 == "rock" and player_2 == "paper":
        print( "Player 2 wins!")

    elif player_1 == "paper" and player_2 == "rock":
        print ("Player 1 wins!")

    elif player_1 == "rock" and player_2 == "scissors":
        print ("Player 1 wins!")

    elif player_1 == "scissors" and player_2 == "rock":
        print ("Player 2 wins")

    elif player_1 == "paper" and player_2 == "scissors":
        print ("Player 2 wins!")

    elif player_1 == "scissors" and player_2 == "paper":
        print ("Player 1 wins!")

print(f"Player 1: {p1_call}\nPlayer 2: {p2_call}\n")
rock_paper_scissors(p1_call, p2_call)

'''
Có thể hiểu tính công bằng bằng cách cho máy tính chọn ngẫu nhiên rock/paper/scissors sau đó nhập thứ tự người chơi.
'''