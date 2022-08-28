from IPython.display import Image
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import seaborn as sns


from google.colab import drive
drive.mount('/content/drive/')

Image('/content/drive/MyDrive/SD_mooncake.png')

img = cv.imread('/content/drive/MyDrive/SD_mooncake.png', cv.IMREAD_COLOR)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

h, w, _ = img.shape

top_left = img[:h//2, w//2:]
top_right = img[h//2:, w//2:]
bottom_left = img[:h//2, :w//2]
bottom_right = img[h//2:, :w//2]
moon_cake = np.zeros((h, w, 3), dtype=np.uint8)
moon_cake[:h//2, :w//2 +1] = top_left
moon_cake[:h//2, w//2:] = top_right
moon_cake[h//2:, :w//2] = bottom_left
moon_cake[h//2:, w//2 +1:] = bottom_right
plt.imshow(cv.cvtColor(moon_cake, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()