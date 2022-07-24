import math

def giaiPTBac2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        x = -b/(2*a)
        return (x, )
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x2, x1)

def main():
    print (giaiPTBac2(1, 1, -2)) #(-2.0, 1.0)
    print (giaiPTBac2(1, 2, 1)) #(-1.0,)
    print (giaiPTBac2(1, 0, 1)) #()
    print (giaiPTBac2(1, 3, -1)) #(-3.302775637731995, 0.30277563773199456)
    print (giaiPTBac2(3, 7, 2)) #(-2.0, -0.3333333333333333)
    
if __name__ == "__main__":
    main()