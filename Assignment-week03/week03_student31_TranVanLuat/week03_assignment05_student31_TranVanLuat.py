import os
def whoWin(player1, player2):
   if player1 == 'keo':
       if player2 == 'bua':
           print('player 2 is the winner')
       elif player2 == 'la':
           print('player 1 is the winner')
       elif player2 == 'keo':
           print('No one is the winner')
           
   if player1 == 'bua':
       if player2 == 'bua':
           print('No one is the winner')
       elif player2 == 'la':
           print('player 2 is the winner')
       elif player2 == 'keo':
           print('player 1 is the winner')
        
            
   if player1 == 'la':
       if player2 == 'bua':
           print('player 1 is the winner')
       elif player2 == 'la':
           print('No one is the winner')
       elif player2 == 'keo':
           print('player 2 is the winner')
        
if __name__ == '__main__':
    player1 = input("Player 1 chooses: ")
    os.system('cls')
    player2 = input("Player 2 chooses: ")
    whoWin(player1, player2)