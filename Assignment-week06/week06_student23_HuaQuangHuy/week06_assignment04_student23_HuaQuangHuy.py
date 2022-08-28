# thay đổi hình ảnh
from pickletools import uint8
import numpy as np
import cv2

pathImage = './additionalFolder/SD_mooncake.png'
#  read image
imageColor = cv2.imread(pathImage, 1)  # flag 1 is color, 0 is gray image

# get shape (size) of image
print(imageColor.shape[0])  # 498 x 505

# crop origin image to 4 part
beginRow = 0
beginColumn = 0
centerRow = imageColor.shape[0] // 2
centerColumn = imageColor.shape[1] // 2
endRow = imageColor.shape[0]
endColumn = imageColor.shape[1]
# part 1
imagePart1 = imageColor[beginRow:centerRow, beginColumn:centerColumn]

# part 2
imagePart2 = imageColor[centerRow:endRow, beginColumn:centerColumn]

# part 3
imagePart3 = imageColor[beginRow:centerRow, centerColumn:endColumn]

# part 4
imagePart4 = imageColor[centerRow:endRow, centerColumn:endColumn]

# merge image
result = np.zeros(
    (imageColor.shape[0], imageColor.shape[1]+1, 3), dtype=np.uint8)
result[beginRow:centerRow, beginColumn:centerColumn+1] = imagePart3
result[beginRow:centerRow, centerColumn:endColumn] = imagePart4
result[centerRow:endRow, beginColumn:centerColumn] = imagePart1
result[centerRow:endRow, centerColumn+1:endColumn] = imagePart2

# save image
cv2.imwrite('./additionalFolder/resultImage04.png', result)


#  show image
# cv2.imshow('window', imageColor)
# cv2.imshow('part1', imagePart1)
# cv2.imshow('part2', imagePart2)
# cv2.imshow('part3', imagePart3)
# cv2.imshow('part4', imagePart4)

cv2.imshow('result', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
