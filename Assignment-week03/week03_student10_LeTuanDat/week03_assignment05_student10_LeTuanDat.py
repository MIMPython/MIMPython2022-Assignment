p1 = input("Player 1 --> Rock, Paper, or Scissors? ")
p1 = p1.lower()
print()
p2 = input("Player 2 --> Rock, Paper, or Scissors? ")
p2 = p2.lower()
print()

if (p1 == "rock"):
    if (p2 == "rock"):
        print("The game is a draw")
    elif (p2 == "paper"):
        print("Player 2 wins!")
    elif (p2 == "scissors"):
        print("Player 1 wins!")
elif (p1 == "paper"):
    if (p2 == "rock"):
        print("Player 1 wins!")
    elif (p2 == "paper"):
        print("The game is a draw")
    elif (p2 == "scissors"):
        print("Player 2 wins!")
elif (p1 == "scissors"):
    if (p2 == "rock"):
        print("Player 2 wins!")
    elif (p2 == "paper"):
        print("Player 1 wins!")
    elif (p2 == "scissors"):
        print("The game is a draw")
