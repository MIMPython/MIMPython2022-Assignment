#To assure the fairness of the game, we will create a 
#program that don't let player see the other player's
# choice by tell players enter number of space to choose
# rock, paper or scissors 
#ahihi
while True:
    a_turn = input("enter number of space to choose"
                   + "\nnumber divide 3 remain 0: rock, remain 1: paper, remain 2: scissor")
    if a_turn == "quit":
        break
    b_turn = input("enter number of space to choose"
                   + "\nnumber divide 3 remain 0: rock, remain 1: paper, remain 2: scissor")
    
    if len(a_turn) % 3 == 0:
        print("A has choosen rock")
        if len(b_turn) % 3 == 0:
            print("B has choosen rock")
            print("draw")
        elif len(b_turn) % 3 == 1:
            print("B has choosen paper")
            print("B won")
        else:
            print("B has choosen scissor")
            print("A won")
            
    if len(a_turn) % 3 == 1:
        print("A has choosen paper")
        if len(b_turn) % 3 == 0:
            print("B has choosen rock")
            print("A won")
        elif len(b_turn) % 3 == 1:
            print("B has choosen paper")
            print("draw")
        else:
            print("B has choosen scissor")
            print("B won")
            
    if len(a_turn) % 3 == 2:
        print("A has choosen scissor")
        if len(b_turn) % 3 == 0:
            print("B has choosen rock")
            print("B won")
        elif len(b_turn) % 3 == 1:
            print("B has choosen paper")
            print("A won")
        else:
            print("B has choosen scissor")
            print("draw")
            
#we can understand fairness in another way: create game for 2 player in two devices,
#so players can't see eachother's choice