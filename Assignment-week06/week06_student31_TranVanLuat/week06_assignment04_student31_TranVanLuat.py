import cv2
import numpy 
import matplotlib.pyplot 

img = cv2.imread('SD_mooncake.png')

elem1 = int(0)
elem2 = int(0)
elem3 = int(249)
elem4 = int(252)

A = []
for i in range(2):
    tempList = []
    for j in range(2):
        tempList.append(img[elem1 + elem3 * i : elem1 + elem3 *(i+1) , elem2 + elem4 * j : elem2 + elem4 * (j + 1) + 1])
    A.append(tempList)

first = cv2.vconcat([A[0][1],A[0][0]])
second = cv2.vconcat([A[1][1],A[1][0]])
third = cv2.hconcat([first,second])

cv2.imshow('Image: ', third)
cv2.waitKey(0)
