import os

def play(player):
    """Single RPS round, returning user outcome boolean"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Let's Play!")
    print('-----------')
    print('')
    print('1) Rock')
    print('2) Paper')
    print('3) Scissor')
    print('')
    
    player_selection = input('{} make a selection (numbers and words accepted): '.format(player))
    
    valid_selection = {
        1: 'rock',
        2: 'paper',
        3: 'scissor',
    }

    try:
        key = int(player_selection)
        if key in valid_selection.keys():
            player_selection = valid_selection[key]
        else:
            print("Invalid selection")
            return play(player)
    except ValueError:
        if player_selection.lower() in valid_selection.values():
            player_selection = player_selection.lower()
        else:
            return play(player)
    return player_selection

def compare(player1 ,player2):
    diff = player1 - player2
    if((diff%2==0 and diff<0) or (diff%2==1 and diff>0)):
        return True # Player 1 won
    else:
        return False # Player 2 won

def rock_paper_scissor():
    """Main entry point for the game"""
    os.system('cls' if os.name == 'nt' else 'clear')

    # present the menu
    print('Rock - Paper - Scissor')
    print('----------------------')
    print('')
    print('1) Quick Draw')
    print('2) Exit')
    print('')
    selection = input('Make a selection (only numbers accepted): ')

    # Check for a integer input
    try:
        selection = int(selection)
    except ValueError:
        return rock_paper_scissor()

    # Check that it's a valid option
    valid_selection = [1, 2]
    if selection not in valid_selection:
        return rock_paper_scissor()

    # at this point, selection is valid. operate on it
    if selection == 1:
        game()
    elif selection == 2:
        exit()

def game():
    player1 = play("player1")
    player2 = play("player2")
    
    if player1 == player2:
        print('\nYOU TIED! TRY AGAIN ...')
        return rock_paper_scissor()

    elif (player1 == 'rock' and player2 == 'paper') \
            or (player1 == 'paper' and player2 == 'scissor') \
            or (player1 == 'scissor' and player2 == 'rock'):
        print("Player 2 WIN")

    else:
        input('\nPlayer 1 WIN')
        return True
        
    print("Thank you for playing")
    
if __name__ == '__main__':
    rock_paper_scissor()
    game()