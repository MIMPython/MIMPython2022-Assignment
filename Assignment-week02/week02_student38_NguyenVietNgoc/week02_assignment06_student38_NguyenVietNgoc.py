import math
 
def quadratic(a, b, c, solution = tuple()):
    # check coefficients
    if (a == 0):
        if (b == 0):
            print (solution)
        else:
            solution = (-c/b, )
            print (solution)
        return
 
    delta = b**2 - 4 * a * c

    # solve the equation
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))

        if x1 > x2:
            solution = (x2, x1)
        else:
            solution = (x1, x2)
        print (solution)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        solution = (x1,)
        print (solution)
    else:
        print (solution)
    solution    
 
a = float(input("Enter coefficient a = "))  # a = 3
b = float(input("Enter coefficient b = "))  # b = 5
c = float(input("Enter coefficient c = "))  # c = -7

quadratic(a, b, c)  # (-2.5733844181517584, 0.9067177514850918)