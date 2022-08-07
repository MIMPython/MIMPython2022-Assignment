from getpass4 import getpass

# Bài tập 5: Rock - paper - scissor
"""
Rules: 
Rock vs paper => paper win
scissor vs paper => scissor win
scissor vs rock => rock win

"""


def checkOption(option):
    while option < 1 or option > 3:
        print("invalid option, please try again")
        return int(getpass("Enter your option..."))


if __name__ == '__main__':
    # Input
    listItem = ['Rock', 'Scissor', 'Paper']
    while True:
        print("1 - rock")
        print("2 - scissor")
        print("3 - paper")
        player1Input = (int(getpass("Enter your option...")))
        result1 = checkOption(player1Input)
        # print(result1)
        if result1 != None:
            player1Input = result1
        player2Input = (int(getpass("Enter your option...")))
        result2 = checkOption(player2Input)
        # print(result2)
        if result2 != None:
            player2Input = result2
    # Output:
        print(f"Player1: {listItem[player1Input - 1]}")
        print(f"Player2: {listItem[player2Input - 1]}")
        if player1Input == player2Input:
            print("draw")
        elif (player1Input == 1 and player2Input == 2) or (player1Input == 2 and player2Input == 3) or (player1Input == 3 and player2Input == 1):
            print("Player 1 win")
        else:
            print("Player 2 win")
