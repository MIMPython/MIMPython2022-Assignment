import cv2
import numpy as np
img =  cv2.imread(r"D:\image.jpg")

img_1 = img[0:246,0:246]
img_2 = img[0:246,258:501]
img_3 = img[252:498,1:247]
img_4 = img[252:498,252:501]


banh_trung_thu = np.concatenate((img_2,img_4),axis=1)
an_kieng = np.concatenate((img_1, img_3), axis=1)

result = np.concatenate((banh_trung_thu,an_kieng), axis=0)
cv2.imshow("ghep anh", result)
cv2.waitKey(10000)

