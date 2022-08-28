print("Bài 8: Conway’s Game Of Life")

"""
Luật chơi GAME OF LIFE
+ Nếu ô có dưới hai hàng xóm thì sẽ chết vì số dân suy giảm
+ Nếu ô có trên ba hàng xóm thì sẽ chết vì số dân quá đông
+ Nếu ô có 2 hoặc 3 hàng xóm thì sống y nguyên và phát triển bền vững
+ Nếu xung quanh ô đã chết có đúng ba ô sống thì nó sống lại
"""
from random import randint
import copy
import time

#Đầu vào
m = int(input("Nhập chiều dài: "))          #Nhập hàng
n = int(input("Nhập chiều rộng: "))         #Nhập cột

ALIVE = 1
DEAD = 0

lst = {}            #Một dictionary chứa giá trị của từng hàng/cột trong tuple
for x in range(m):
    for y in range(n):
        k = randint(0,1)
        if k == 1:
            lst[(x, y)] = ALIVE
        else:
            lst[(x, y)] = DEAD

conway = copy.deepcopy(lst)     #Mảng sao chép của lst
print(conway)
#Hàng xóm ban đầu
for x in range(m):
    for y in range(n):
        print(conway[(x, y)], end = " ")
    print()

print()

#Thuật toán Game of life
while True:
    for i in range(1, m-1):
        for j in range(1, n-1):
            hangtren = i-1
            hangduoi = i+1
            cottrai = j-1
            cotphai = j+1

            #Đếm số hàng xóm lân cận
            neigh = 0
            if conway[(hangtren, cottrai)] == ALIVE:
                neigh += 1
            if conway[(hangtren, j)] == ALIVE:
                neigh += 1
            if conway[(hangtren, cotphai)] == ALIVE:
                neigh += 1
            if conway[(i, cottrai)] == ALIVE:
                neigh += 1
            if conway[(i, cotphai)] == ALIVE:
                neigh += 1
            if conway[(hangduoi, cottrai)] == ALIVE:
                neigh += 1
            if conway[(hangduoi, j)] == ALIVE:
                neigh += 1
            if conway[(hangduoi, cotphai)] == ALIVE:
                neigh += 1

            print(f"Số hàng xóm lân cận ở vị trí ({i}, {j}) là: {neigh}")

            #Nếu ô sống có 2 hoặc 3 hàng xóm thì sẽ sống
            if conway[(i, j)] == ALIVE and (neigh == 2 or neigh == 3):
                conway[(i, j)] = ALIVE
            #Nếu ô chết có 3 hàng xóm thì sống
            elif conway[(i, j)] == DEAD and neigh == 3:
                conway[(i, j)] = ALIVE
            #Các TH còn lại
            else:
                conway[(i, j)] = DEAD 

    print(conway)
    for x in range(m):
        for y in range(n):
            print(conway[(x, y)], end = " ")
        print()
    
    time.sleep(5)
