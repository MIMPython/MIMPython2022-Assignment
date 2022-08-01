#a) Trò kéo-búa-bao  

# Quy ước:
# Kéo thắng bao
# Bao thắng búa
# Búa thắng kéo
# Giống nhau hòa
# Người chơi nhập từ 1-3 theo quy ước: 1 = Búa, 2 = Bao, 3 = Kéo

import random

#Nười chơi nhập lựa chọn từ 1-3
player1 = int(input('Enter Player1 selection: '))
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
print('|')
Player2 = int(input('Enter Player2 selection: '))

#In ra lựa chọn của người chơi 1
def print_selection_player1(player1):
   if player1 == 1:
      print('player1 choose rock')
   if player1 == 2:
      print('player1 choose paper')
   if player1 == 3:
      print('player1 choose scissors')

#In ra lựa chọn của người chơi 2
def print_selection_Player2(Player2):
   if Player2 == 1:
      print('Player2 choose rock')
   if Player2 == 2:
      print('Player2 choose paper')
   if Player2 == 3:
      print('Player2 choose scissors')
   

def rock_paper_scissors(a, b):
   if a == b:
      print('The game is a tie')                               
   if a == 1:
      if b == 2:
         print('Player2 win!')
      if b == 3:
         print('Player1 win!')
   if a == 2:
      if b == 1:
         print('Player1 win!')
      if b == 3:
         print('Player2 win!')
   if a == 3:
      if b == 1:
         print('Player2 win!')
      if b == 2:
         print('Player1 win!')

print_selection_player1(player1)
print_selection_Player2(Player2)
rock_paper_scissors(player1, Player2)


#  b)Ta có thể in | như trên để người thứ 2 không thấy lựa chọn của người thứ nhất