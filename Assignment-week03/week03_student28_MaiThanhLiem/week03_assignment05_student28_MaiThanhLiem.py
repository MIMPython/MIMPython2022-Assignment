import time, numpy, os

# import time for getting current time
# import numpy for the floor function
# import os to interacting with keyboard


def rock_paper_scissors_game():
    while True:
        # a.
        # print("\nEnter your choices: 0 = Scissors, 1 = Rock, 2 = Paper")  # rules
        # choices = ["scisssors", "rock", "paper"]
        # print("A's choice:")
        # x = int(input())
        # print("B's choice:")
        # y = int(input())
        # b.
        choices = ["scisssors", "rock", "paper"]
        print("\nRock - Paper - Scissors game:")
        print("A's turn:")
        x = int(numpy.floor(time.time()) % 3)
        # x will get "random" value in range (0, 3)
        os.system("pause")
        # interacting with keyboard, only continue after press any key
        print("B's turn:")
        y = int(numpy.floor(time.time()) % 3)
        os.system("pause")

        if x < len(choices) and y < len(choices):  # checking reasonable choices
            print("\nA choose: ", choices[x], ", B choose: ", choices[y], "\n")
            if x == y:
                print("The game is draw!")
            elif x == 2 and y == 0:
                print("B wins")
            elif x == 0 and y == 2:
                print("A wins")
            elif x == y - 1:
                print("B wins")
            elif x == y + 1:
                print("A wins")
        else:
            print("Please re-enter your choices")  # invalid input for choices
        os.system("pause")


rock_paper_scissors_game()

# c. Hard to determine what is "Fair" here. In this situation, randomness may be the best choice.
