def halfPyramid(rows):
    print ("Half Pyramid")
    for i in range (rows):
        for j in range (i+1):
            print ("*", end = "")
        print ("")

def invertedHalfPyramid(rows):
    print ("Inverted Half Pyramid")
    for i in range (rows):
        for j in range (rows - i):
            print ("*", end = "")
        print ("")
        
def hollowInvertedHalfPyramid(rows):
    print ("Hollow Inverted Half Pyramid")
    for i in range (rows):
        for j in range (rows - i):
            if i == 0 or j == 0 or j == rows - i - 1:
                print ("*", end = "")
            else:
                print (" ", end = "")
        print ("")
        
def fullPyramid(rows):
    print ("Full Pyramid")
    for i in range (rows):
        for j in range (rows - i -1):
            print (" ", end = "")
        for j in range (i+1):
            print ("* ", end = "")
        print ("")
        
def invertedFullPyramid(rows):
    print ("Inverted Full Pyramid")
    for i in range (rows):
        for j in range (i):
            print (" ", end = "")
        for j in range (rows - i):
            print ("* ", end = "")
        print ("")

def hollowFullPyramid(rows):
    print ("Hollow Full Pyramid")
    for i in range (rows):
        for j in range (rows - i -1):
            print (" ", end = "")
        for j in range (i+1):
            if i == rows - 1 or j == 0 or j == i:
                print ("* ", end = "")
            else:
                print ("  ", end = "")
        print ("")
        
halfPyramid(6)
invertedHalfPyramid(6)
hollowInvertedHalfPyramid(6)
fullPyramid(6)
invertedFullPyramid(6)
hollowFullPyramid(6)