from cmath import sqrt

def foo(a, b, c):
    tup = ()
    if a == 0:
        if b == 0:
            if c == 0:
                print(tup)
            else:
                print(tup)
        else:
            tup += -c/b
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print(tup)
        elif delta == 0:
            tup += (-b/(2*a) , )
        else:
            tup += ((-b - sqrt(delta))/(2*a) , )
            tup += ((-b + sqrt(delta))/(2*a) , )
            print (tup)
            
if __name__ == '__main__':

    foo(1, 2, 1) # (-1, )

    