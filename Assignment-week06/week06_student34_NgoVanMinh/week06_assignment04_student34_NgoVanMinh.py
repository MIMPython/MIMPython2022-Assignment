import cv2 as cv
import numpy as np

if __name__ == '__main__':
    x = 0
    y = 0
    h = 250
    w = 250
    img = cv.imread("cake.png")

    #Ăn
    crop_img1 = img[y:y + h, x:x + w]
    cv.imwrite("1.png", crop_img1)

    #Trung thu
    crop_img2 = img[250:250+ h,   250:250 + w]
    cv.imwrite("2.png", crop_img2)

    #Bánh
    crop_img3 = img[0:0 + h, 250:250 + w]
    cv.imwrite("3.png", crop_img3)

    #Kiêng
    crop_img4 = img[250:250 + h, 0:0 + w]
    cv.imwrite("4.png", crop_img4)

    img_read1 = cv.imread("1.png", cv.IMREAD_COLOR)
    img_read2 = cv.imread("2.png", cv.IMREAD_COLOR)
    img_read3 = cv.imread("3.png", cv.IMREAD_COLOR)
    img_read4 = cv.imread("4.png", cv.IMREAD_COLOR)

    col1 = np.vstack([img_read3, img_read1])
    col2 = np.vstack([img_read2, img_read4])

    result = np.hstack([col1, col2])
    k = cv.waitKey(0)
    cv.imwrite("result.png", result)