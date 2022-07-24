# (1) Half Pyramid
def halfPyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print()


halfPyramid(6)

# (2) Inverted half pyramid


def invertedHalfPyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()


invertedHalfPyramid(6)

# (3) Hollow inverted half pyramid


def hollowInvertedHalfPyramid(n):
    for i in range(n):
        for j in range(n-i):
            if i == 0 or j == 0 or j == n-i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


hollowInvertedHalfPyramid(6)

# (4) Full Pyramid


def fullPyramid(n):
    for i in range(1, n+1):
        print(("* "*i).center(2*n-1))


fullPyramid(6)

# (5) Inverted full pyramid


def invertedFullPyramid(n):
    for i in range(n, 0, -1):
        print(("* "*i).center(2*n-1))


invertedFullPyramid(6)

# (6) Hollow full pyramid


def hollowFullPyramid(n):
    count = 0
    for i in range(1, n+1):
        if i in range(3, n):
            print(("*"+" "*(i+count)+"*").center(2*n-1))
            count += 1
        else:
            print(("* "*i).center(2*n-1))


hollowFullPyramid(6)
