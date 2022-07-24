#Half Pyramid
from socket import AI_V4MAPPED


print("Half Pyramid")
for i in range( 1, 7 ):
    print("*"*i)

#Inverted Half Pyramid 
print()
print("Inverted Half Pyramid")
for i in range(6):
    print("*"*(6-i))

#Hollow Inverted Half Pyramid
print()
print("Hollow Inverted Half Pyramid")
print("*"*6)
for i in range(4):
    print("*"," "*(3-i),"*",sep="")
print("*")

#Full Pyramid 
print()
print("Full Pyramid ")
pyramid= "     *"
PYRAMID = list()
PYRAMID.append(pyramid)
print(pyramid)
def str (x):
    return pyramid[0:(5-x-1)] +"* "+pyramid[(5-x) : 10]
for i in range(5):
    PYRAMID.append(str(i)) 
    pyramid = PYRAMID[i+1]
    print(pyramid)

#Inverted  Full Pyramid
print()
print("Inverted  Full Pyramid")
for i in range(6):
    print(PYRAMID[5 - i])

#Hollow Full Pyramid 
print()
print("Hollow Full Pyramid")
pyramid= "     *"
print(pyramid)
def hollow (x):
    return pyramid[0:(5-x-1)] + "*" + " " *(2*(x + 1) - 1) + "*"
for i in range(4): 
    pyramid = hollow(i)
    print(pyramid)
print("* "*6)