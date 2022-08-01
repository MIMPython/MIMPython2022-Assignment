def keoBuaBao(player1, player2):
    if player1 == 1:
        if player2 == 1:
            print("Drawn")
        elif player2 == 2:
            print("Player2 win")
        elif player2 == 3:
            print("Player 1 win")
        else:
            print("Retype!")
    elif player1 == 2:
        if player2 == 1:
            print("Player1 win")
        elif player2 == 2:
            print("Drawn")
        elif player2 == 3:
            print("Player2 win")
        else:
            print("Retype!")
    elif player1 == 3:
        if player2 == 1:
            print("Player2 win")
        elif player2 == 2:
            print("Player1 win")
        elif player2 == 3:
            print("Drawn")
        else:
            print("Retype!")
    else:
            print("Retype!")
a = int(input("Moi nguoi choi chon Keo-1 Bua-2 Bao-3: "))
b = int(input("Moi nguoi choi chon Keo-1 Bua-2 Bao-3: "))
keoBuaBao(a,b)