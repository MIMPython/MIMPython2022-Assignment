import math

def foo(a, b, c):
    if (a == 0):
        if (b == 0):
            print("(  )");
        else:
            print("(", -c / b, ")");
        return;
    
    delta = b * b - 4 * a * c;
   
    if (delta > 0):
        x1 = ((-b + math.sqrt(delta)) / (2 * a));
        x2 = ((-b - math.sqrt(delta)) / (2 * a));
        print("(", x1, ",", x2, ")");
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("(", x1, ",  )");
    else:
        print("(  )");

foo(5, 2, -3) # ( 0.6 , -1.0 )
foo(1, -2, 1) # ( 1.0 ,  )
foo(1, -1, 2) # (  )