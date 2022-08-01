# Bài tập 5. (rock-paper-scissors game)
import random

if __name__ == "__main__":
    A = random.choices(["rock", "paper", "scissors"])
    B = random.choices(["rock", "paper", "scissors"])
    print((A, B))
    if A == B:
        print("Two players draw")
    else:
        if A == ["rock"] and B == ["paper"]:
            print("Player A loses the game")
        if A == ["rock"] and B == ["scissors"]:
            print("Player A wins the game")
        if A == ["paper"] and B == ["rock"]:
            print("Player A wins the game")
        if A == ["paper"] and B == ["scissors"]:
            print("Player A loses the game")
        if A == ["scissors"] and B == ["rock"]:
            print("Player A loses the game")
        if A == ["scissors"] and B == ["paper"]:
            print("Playes A wins the game")
    """(['scissors'], ['rock'])
        Player A loses the game"""