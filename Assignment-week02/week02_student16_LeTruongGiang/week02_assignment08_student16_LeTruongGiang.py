#rows = int(input("Enter number of rows: "))

rows = 6
print("Half Pyramid")
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()

print("Inverted Half pyramid")
for i in range(rows):
    for j in range(rows - i):
        print("*", end="")
    print()
    
print("Hollow Inverted Half pyramid")
for i in range(rows):
    for j in range(rows):
        if i == 0 or j == 0 or i + j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
print("Full pyramid")
for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
    
print("Inverted full pyramid")
for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for j in range(rows-i):
        print("*", end=" ")
    print()
    
print("Hollow Full pyramid")
for i in range(rows):
    for j in range(rows-i-1):
        print(' ', end='') # printing space required and staying in same line
    for j in range(2*i+1):
        if j==0 or j==2*i or i==rows-1:
            print('*',end='')
        else:
            print(' ', end='')
    print() 


print("Hollow Inverted Full pyramid")
print(rows * "* ")
for i in range(rows-2,0,-1):
    print((rows-i-1)* " " +  "*" + (2*i -1)*" " + "* ")
print((rows-1 )* " " + "* ")


print("Hollow Full pyramid")
print((rows-1)*" " + "* ")
for i in range(0,rows-2,1):
    print((rows-i-2)* " " + "*" + (2*i +1)*" " + "* ")
print(rows * "* ")
    
        

