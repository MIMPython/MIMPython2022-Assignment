# a)

def rule_game():
    while True: 
        person_first = input("Rock, paper, scissors:").rstrip()
        person_second = input("Rock, paper, scissors:").rstrip()
        if person_first == 'rock' and person_second == 'paper':
            print("The second person is the winner.")
            break
        elif person_first == 'rock' and person_second == 'scissors':
            print("The first person is the winner.")
            break
        elif person_first == 'paper' and person_second == 'scissors':
            print("The second person is the winner.")
            break
        elif person_first == 'paper' and person_second == 'rock':
            print("The first person is the winner.")
            break
        elif person_first == 'paper' and person_second == 'scissors':
            print("The second person is the winner.")
            break
        elif person_first == 'scissors' and person_second == 'rock':
            print("The first person is the winner.")
            break
        else:
            print("No one is the winner.")
            print("Play agian.")
rule_game()
#b)
import random
values = ['rock', 'paper', 'scissors']
choices = [1, 2, 3]
dict_choices = dict(zip(choices, values))
def random_choices():
    random_choice = random.randint(1,3)
    return random_choice
def choice_player():
    choice = input("Rock, paper, scissors:").rstrip()
    return choice
def rule_game_1():
    random_player = dict_choices[random_choices()]
    choice_of_player = choice_player()
    if choice_of_player == 'rock' and random_player == 'paper':
        print("Player random is the winner.")
    elif choice_of_player == 'paper' and random_player == 'rock':
        print("Player  is the winner.")
    elif choice_of_player == 'rock' and random_player == 'scissors':
        print("Player is the winner.")
    elif choice_of_player == 'scissors' and random_player == 'rock':
        print("Player random is the winner.")
    elif choice_of_player == 'scissors' and random_player == 'paper':
        print("Player is the winner.")
    elif choice_of_player == 'paper' and random_player == 'scissors':
        print("Player random is the winner.")
    else:
        print("No one is the winner.")
rule_game_1()

#c)
"""
Theo như câu b), em làm thì sẽ cho 1 người có thể lựa chọn tùy theo ý của mình, còn 1 người chơi 
sẽ lựa chọn ngẫu nhiên.Do vậy, công bằng ở đây có thể hiểu là không ai biết trước được người kia 
sẽ lựa chọn đấm, lá hay kéo.  
"""