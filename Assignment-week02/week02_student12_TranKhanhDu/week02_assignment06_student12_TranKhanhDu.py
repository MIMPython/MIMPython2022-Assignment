import math
def solvingEquals(a, b,c):
    if a == 0:
        if b != 0:
            print("equals has only one solution is" + str(-c/b))
        elif b == 0: 
            if c == 0:
                print("equals has countless solutions")
            else:
                print("equals has no solution")
    else:
        delta = b**2 -4*a*c
        if delta > 0:
            print("equals has two solutions are: " + str((-b+math.sqrt(delta))/2/a) +
                  " and " + str((-b-math.sqrt(delta))/2/a))
        elif delta == 0:
            print("equals has one solution is " + str(-b/2/a))
        else:
            print("equals has no solution")
            
#test function
solvingEquals(1,2,3)
solvingEquals(1,2,1)
solvingEquals(1,0,1)
solvingEquals(1,1,-2)