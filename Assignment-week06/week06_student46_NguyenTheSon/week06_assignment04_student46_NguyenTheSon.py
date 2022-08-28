from PIL import Image
import numpy as np
# Bài 4:

img = Image.open("additionalFolder/SD_mooncake.png")

box = (250,0,500,250)
img1 = img.crop(box)
img1.save("additionalFolder/SD_mooncake_1.png")

box = (0,0,250,250)
img2 = img.crop(box)
img2.save("additionalFolder/SD_mooncake_2.png")

box = (0, 250, 250, 500)
img3 = img.crop(box)
img3.save("additionalFolder/SD_mooncake_3.png")

box = (250, 250, 500, 500)
img4 = img.crop(box)
img4.save("additionalFolder/SD_mooncake_4.png")

array_img1 = np.array(img1)
array_img2 = np.array(img2)
array_img3 = np.array(img3)
array_img4 = np.array(img4)
row_1 = np.hstack((array_img1, array_img4))
row_2 = np.hstack((array_img2, array_img3))

new_array_img = np.vstack((row_1, row_2))
new_img = Image.fromarray(new_array_img)
new_img.save("additionalFolder/SD_mooncake_final.png")
new_img.show()