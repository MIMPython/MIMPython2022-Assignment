x=int(input())
str=input()
l=ord('A')
r=ord('Z')
for i in str:
    if (ord(i)+x>r) : print(chr(ord(i)+x-r+l-1),end='')
    else : print (chr(ord(i)+x))
