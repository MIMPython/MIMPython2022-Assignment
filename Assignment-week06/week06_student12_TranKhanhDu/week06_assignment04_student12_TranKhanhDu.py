import cv2
picturePath = 'D:\\VisualCode\\Python\\MIM2022Python\\SD_mooncake.png'
img = cv2.imread(picturePath)

#get length and wigth
widthOfPicture = img.shape[0]
lengthOfPicture = img.shape[1]

#because the length ofpicture is an odd number so i will change it to an even number
afterPicture = cv2.resize(img, (0,0), fx=506/505, fy = 1)

# store parts of picture in each varibles
piece1 = afterPicture[0:249, 0:253]
piece2 = afterPicture[0:249, 253:506]
piece3 = afterPicture[249:498, 0:253]
piece4 = afterPicture[249:498, 253:506]

#change the position of pieces
afterPicture[0:249, 0:253] = piece2
afterPicture[0:249, 253:506] = piece4
cv2.imshow("picture after edit", piece1)
afterPicture[249:498, 0:253] = piece1
afterPicture[249:498, 253: 506] = piece3
#làm thế nào để ghép các ảnh với nhau vậy??
cv2.imshow("picture after edit", afterPicture)
cv2.waitKey(0)