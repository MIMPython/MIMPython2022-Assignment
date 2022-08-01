
print("Fill in file player_1.txt and player_2.txt your choose rock-scissor-paper")
print("----------------------------------------")
with open("player_1.txt","r") as file_1:
    with open("player_2.txt","r") as file_2:
        one_1 = file_1.read().splitlines()
        two_2 = file_2.read().splitlines()

one = one_1[-1]
two = two_2[-1]
print(one)
print(two)

if one== "rock":
    if two == "rock":
        print("Draw")
    elif two == "paper":
        print("Player 2 is Winner")
    else:
        print("Player 1 is Winner")
if one == "scissor":
    if two== "paper":
        print("Player 1 is Winner")
    elif two== "rock":
        print("Player 2 is Winner")
    else:
        print("Draw")
if one == "paper":
    if two == "scissor":
        print("Player 2 is Winner")
    elif two == "rock":
        print("Player 1 is Winner")
    else:
        print("Draw")