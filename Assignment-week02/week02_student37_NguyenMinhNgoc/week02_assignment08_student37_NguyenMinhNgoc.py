#(1) Half Pyramid
from turtle import end_fill
n = 6
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end="")
    print()

# (2) Inverted Half Pyramid
def inverted_half_pyramid(num):
    for i in range (num,0,-1):
        print("*"*i)

# (3) Hollow Inverted Half Pyramid

# (4) Full Pyramid

def full_pyrami(num):
    for i in range(0,num):
        for j in range(num - i - 1):
            print(end = " ")
        for j in range(i + 1):
            print("*", end= " ")
        print()

# (5) Inverted Full Pyramid
def inverted_full_pyramid(num):
    for i in range (num,0,-1):
        print(" "*(num-i)+"* "*i)

# (6) Hollow Full Pyramid




if __name__ == '__main__':

# 4) Full Pyramid
    full_pyrami(6)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#* * * * * * 

#2) Inverted Half Pyramid
    inverted_half_pyramid(6)
#******
#*****
#****
#***
#**
#*  

#5) Inverted Full Pyramid
    inverted_full_pyramid(6)
#* * * * * *
#* * * * *
# * * * *
#  * * *
#   * *
#    *  

    