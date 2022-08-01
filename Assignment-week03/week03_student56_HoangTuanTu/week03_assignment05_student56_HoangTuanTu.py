import os

# Idea is using OS module and os.system('CLS') to clear screen, so player2 can't see player1 Choise
# I have another version of this game using pygame and play with computer!


# Input Player name
def nameOfPlayer():
    player1Name = str(input("Input first player's name: "))
    player2Name = str(input("Input seccond player's name: "))
    return player1Name,player2Name

# Let player @player choise
def playerChoise(player):
    os.system('CLS')
    onScreenTitle = "Input your choise: "
    print(player,"turn!")
    choise = {1:"Rock" , 2:"Paper", 3: "Scissors"}
    while True:
        choiseKey = False
        print(choise)
        pick = input(onScreenTitle)
        # Check player input number or string
        try:
            pick = int(pick)
            choiseKey = True
        except:
            pick=pick.capitalize()

        # return value
        if (choiseKey):
            if pick>=1 and pick<=3:
                return choise[pick]
            else:
                onScreenTitle = "Please input not input number from 1 to 3 or Rock/Paper/Scissors: "
        else:
            if pick in choise.values():
                return pick
            else:
                onScreenTitle = "Please input not input number from 1 to 3 or Rock/Paper/Scissors: "

# Choise stop or not ?
def choiseStop():
    print("Do you want to coutinue? Yes or No?")
    pick = str(input("Your choise: ").capitalize())
    return (pick)

# Users want to stop or not
def stopGame():
    pick = choiseStop()
    while pick!="Yes" and pick != "No":
        print("Wrong input value!")
        pick = choiseStop()
    return pick == "Yes"           


# If win/lose/draw
def win(player):
    print("\nCongratulation! {} have won!".format(player))
def lose(player):
    print("{} have lost! Better try next time!".format(player))
def draw():
    print("Two player have drawn!")
# Check win or lose
def checkWinLose(playerPick,playerName):
    player1Name,player2Name = playerName

    for i in range(len(playerPick)):
        print("Player {} choise: {}" .format(playerName[i],playerPick[i]))

    if playerPick[0]==playerPick[1]:
        draw()

    elif (playerPick[0]=="Rock"):
        if (playerPick[1]== "Paper"):
            win(player2Name)
            lose(player1Name)
        else:
            win(player1Name)
            lose(player2Name)
    elif (playerPick[0]=="Paper"):
        if (playerPick[1] == "Rock"):
            win(player1Name)
            lose(player2Name)
        else:
            win(player2Name)
            lose(player1Name)
    else:
        if (playerPick[1] == "Rock"):
            win(player2Name)
            lose(player1Name)
        else:
            win(player1Name)
            lose(player2Name)

# Print Rule of the game
def rule():
    print("""
+ Player 1 will always pick first then player 2 turn
+ After each choise, if it Available it will clear screen and orther player can only see
after all have choise and game have done.
+ Player input number or string if it is: 1 or "Rock" , 2 or "Paper" and 3 or "Scissors".
After game have done, program will apear for player choise countinue or stop.
+ Simple Rock-Paper-Scissors rule is: Rock<Paper<Scissors and Scissors<Rock
That all done Ready to play ?
            """)
    ready = ""
    while True:
        ready = str(input("Ready or not ?(Yes or No?): ")).capitalize()
        if ready=="Yes" or ready== "No":
            break
        print("Wrong input!")
    return ready == "Yes"

# main method
if __name__ == "__main__":
    os.system('CLS')
    ready = rule()
    if ready:
        os.system('CLS')
        player1Name ,player2Name = nameOfPlayer()
        playerName = list((player1Name + "/" + player2Name).split("/"))
        playerPick = [" "," "]
        goOn = True

        # main loop game
        while (goOn):
            os.system('CLS')
            
            pick = playerChoise(player1Name)
            playerPick[0] = pick

            pick = playerChoise(player2Name)
            playerPick[1] = pick

            os.system('CLS')

            checkWinLose(playerPick,playerName)
            print("\n\n\n")     
            goOn = stopGame()
        print("Thank for playing game !")
    print("Bye!")