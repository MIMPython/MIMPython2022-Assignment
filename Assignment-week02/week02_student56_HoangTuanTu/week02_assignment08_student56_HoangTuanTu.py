def halfPyramid():
    for i in range (1,7):
        print("*"*i)

def invertedHalfPyramid():
    for i in range (6,0,-1):
        print("*"*i)

def hollowInvertedHalfPyramid():
    for i in range (6,0,-1):
        if i == 1 or i == 6:
            print("*"*i)
        else:
            for j in range (1,7):
                if (j==i or j ==1):
                    print("*",end = "")
                else:
                    print(end=" ")
            print()
            

def fullPyramid():
    for i in range (1,7):
        print(" "*(6-i)+"* "*i)

def invertedFullPyramid():
    for i in range (6,0,-1):
        print(" "*(6-i)+"* "*i)

def hollowInvertedFullPyramid():
    for i in range (1,7):
        print(" "*(6-i),end="")
        if i == 1 or i == 6:
            print("* "*i)
        else:
            for j in range (1,7):
                if (j==i or j ==1):
                    print("*",end = " ")
                else:
                    print(end="  ")
            print()

if __name__ == '__main__':
    halfPyramid()
    print()

    invertedHalfPyramid()
    print()

    hollowInvertedHalfPyramid()
    print()

    fullPyramid()
    print()

    invertedFullPyramid()  
    print()

    hollowInvertedFullPyramid()
     