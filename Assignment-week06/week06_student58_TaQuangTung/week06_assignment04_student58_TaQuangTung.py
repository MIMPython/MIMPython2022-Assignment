print("Bài 4: Savoury Days")

import cv2      # Tải thư viện: pip install opencv-python
import numpy as np


pathLink = r'D:\MIM Python\week06_student58_TaQuangTung\additionalFolder\mooncake.jpg'
img = cv2.imread(pathLink)

#Hiển thị ảnh ban đầu
cv2.imshow('MOONCAKE', img)
print(img.shape)        #Kích cỡ ảnh ban đầu
#Giữ ảnh ban đầu
cv2.waitKey()


#Trình cắt ảnh
img1 = img[0:249, 0:252]
cv2.imshow('Ăn', img1)
cv2.waitKey()

img2 = img[0:249, 253:505]
cv2.imshow("Bánh", img2)
cv2.waitKey()

img3 = img[249:498, 0:252]
cv2.imshow("Kiêng", img3)
cv2.waitKey()

img4 = img[249:498, 253:505]
cv2.imshow("Trung Thu", img4)
cv2.waitKey()


#Ghép ảnh lại với nhau: "Bánh Trung Thu ăn kiêng" - 2413
gheptren = cv2.hconcat([img2, img4])
cv2.imshow("Hàng đầu", gheptren)
ghepduoi = cv2.hconcat([img1, img3])
cv2.imshow("Hàng sau", ghepduoi)
cv2.waitKey()

#Ghép ảnh hoàn thiện
tong = np.concatenate((gheptren, ghepduoi), axis = 0)
cv2.imshow("2413", tong)
cv2.waitKey()
