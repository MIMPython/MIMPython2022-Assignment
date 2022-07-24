# Bài tập 8, vẽ các hình
# (1) Half Pyramid

def drawHalfPyramid(width, heigh):
    for i in range(0, heigh):
        for j in range(0, width):
            if i >= j:
                print("*", end="")
            else:
                print("", end="")
        print("")

# (2) Inverted Half Pyramid


def drawInvertedHalfPyramid(width, heigh):
    for i in range(0, heigh):
        for j in range(0, width):
            if i <= j:
                print("*", end="")
            else:
                print("", end="")
        print("")


# 3, Hollow Inverted Half Pyramid
def drawHollowInvertedHalfPyramid(width, heigh):
    for i in range(0, width):
        print("*", end="")
    print("")

    for i in range(1, heigh):
        for j in range(0, width):
            if j == 0 or j == width - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

# 4: Full Pyramid
# width: 11, heigh = 6


def drawFullParamid(width, heigh):
    for i in range(0, heigh):
        for j in range(0, width):
            if(i + j == heigh - 1):
                print("* ", end="")
                for k in range(0, i):
                    print("* ", end="")
                print("")

            else:
                print(" ", end="")
        print("")

# 5, InvertedFullParamid


def drawInvertedFullParamid(width, heigh):
    for i in range(0, heigh):
        for j in range(0, width):
            if(i == j):
                print("* ", end="")
                for k in range(0, heigh - 1 - i):
                    print("* ", end="")
                print("")

            else:
                print(" ", end="")
        print("")

# 6, HollowFullParamid


def drawHollowFullParamid(width, heigh):
    for i in range(0, heigh):
        for j in range(0, width):
            if(i + j == heigh - 1):
                print("* ", end="")
                if (i != 0):
                    if (i < heigh - 1):
                        print((2*(i-1))*" " + "*", end="")
                    else:
                        print(i * "* ", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == '__main__':
    print("Hình 1: ")
    drawHalfPyramid(6, 6)
    print("Hình 2")
    drawInvertedHalfPyramid(6, 6)
    print("Hình 3")
    drawHollowInvertedHalfPyramid(6, 6)
    print("Hình 4")
    drawFullParamid(11, 6)
    print("Hình 5")
    drawInvertedFullParamid(11, 6)
    print("Hình 6")
    drawHollowFullParamid(11, 6)
