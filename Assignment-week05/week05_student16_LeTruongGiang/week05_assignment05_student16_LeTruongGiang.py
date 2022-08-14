#a
def while_():
    i = 1
    while 1 > 0:
        print(f"{i} Sleep tight")
        i+=1
#b
def for_():
    A = [0]
    for i in A:
        print(i)
        A.append(i+1)

#c
def for_2(): 
    for i, j in enumerate(iter(bool, True)):
        print(i)
for_2()
