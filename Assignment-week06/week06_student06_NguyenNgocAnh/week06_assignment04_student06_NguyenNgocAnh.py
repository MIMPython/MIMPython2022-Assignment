import cv2
import numpy as np

path = "additionalFolder/week06_assignment04_student06_NguyenNgocAnh_image_input.png"
image = cv2.imread(path)
height = image.shape[0]
width = image.shape[1]
image = image[:height, 1 :width - 4]

centerY = image.shape[0]//2
centerX = image.shape[1]//2 



up_right_banh = image[:centerY - 1, centerX + 1:]
down_right_trung_thu = image[centerY:, centerX + 1: image.shape[1]-1]
up_left_an = image[:centerY - 1, :centerX - 1]
down_left_kieng = image[centerY + 1:, :centerX]
up_right_banh = cv2.resize(up_right_banh, [up_left_an.shape[1] + 2, up_left_an.shape[0] + 1])

up = np.concatenate((up_right_banh,down_right_trung_thu), axis=1)
down = np.concatenate((up_left_an,down_left_kieng), axis=1)
image_output = np.concatenate((up,down), axis=0)
cv2.imwrite('additionalFolder/week06_assignment04_student06_NguyenNgocAnh_image_output.png', image_output)