def printTicTacToe(ticTac):
    for i in range(len(ticTac)):
        if i!=0:
            print(("_"*5+"|")*3)
        else:
            print(("_"*5+".")*3)
        print((" "*5+"|")*3)
        for j in range(3):
            print("  "+str(ticTac[i][j]),end="  |")
        print()
    print(("_"*5+"|")*3)

def winner(ticTac):
    diagonalLine = []
    for i in range (0,3):
        diagonalLine.append(ticTac[i][i])
    diagonal = "".join(diagonalLine)
    if diagonal == "XXX" or diagonal == "OOO":
        return False

    secDiagonalLine = []
    for i in range (2,-1,-1):
        secDiagonalLine.append(ticTac[i][i])
    secDiagonal = "".join(secDiagonalLine)
    if secDiagonal == "XXX" or secDiagonal == "OOO":
        return False

    for i in range(0,3):
        row = "".join(ticTac[i])

        if row=="XXX" or row =="OOO":
            return False

        col = "".join([ticTac[0][i],ticTac[1][i],ticTac[2][i]])
        if col=="XXX" or col =="OOO":
            return False

    return True

def checkDraw(check):
    for i in range(3):
        for j in range(3):
            if (check[i][j]==True):
                return False
    return True

ticTac = [[],[],[]]
check = [[],[],[]]
x = "X"
o = "O"
u = "-"

def createGame():
    for i in range(3):
        for j in range (3):
            ticTac[i].append(u)
            check[i].append(True)
 
def format(index):
    index-=1
    if index<0 or index>2:
        index = 2
    return index

if __name__ == "__main__":
    draw = False
    createGame()
    player1 = str(input("Input Player 1's name: "))
    player2 = str(input("Input Player 2's name: "))
    printTicTacToe(ticTac)
    player = 1
    while winner(ticTac):
        if checkDraw(check):
            draw = True
            break


        print("Player",player == 1 and player1 or player2, "Turn!")
        col,row = map(int,input("Input move (x y) start at x=1 and y = 1: ").split())
        row = format(row)
        col = format(col)

        if check[row][col]:
            if (player==1):
                check[row][col] = False
                ticTac[row][col] = x 
                player = 2
            else:
                check[row][col] = False
                ticTac[row][col] = o      
                player = 1
            printTicTacToe(ticTac)
        else:
            print("That place is not empty")

    if draw:
        print("Game draw!")
    else:
        print("Congratulation player",player == 1 and player2 or player1,"has won the game!")

