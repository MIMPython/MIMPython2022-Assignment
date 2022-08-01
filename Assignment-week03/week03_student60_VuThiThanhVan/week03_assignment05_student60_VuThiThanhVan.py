
def game (a,b):
    if  a== 'rock' and b== 'paper' :
        return 'b win'
    if a=='rock' and b=='scissors':
        return 'a win'
    if a=='paper' and b=='scissors':
        return 'b win'
    if a=='paper' and b=='rock':
        return 'a win'
    if a=='scissors' and b=='rock':
        return 'b win'
    return 'a win'
a=input()
b=input()
if a!=b :
    print (game(a,b))
     