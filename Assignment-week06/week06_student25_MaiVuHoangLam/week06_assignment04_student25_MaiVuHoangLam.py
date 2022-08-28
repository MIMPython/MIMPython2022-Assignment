import cv2

# read file
path = 'additionalFolder/SD_mooncake.png'
img = cv2.imread(path)

# take size
(height, width, depth) = img.shape  # width=505, height=498, depth=3

# crop part
p1 = img[0:249, 0:249]
p2 = img[249:505, 0:249]
p3 = img[0:250, 251:500]
p4 = img[248:498, 252:501]

# collage part
p34 = cv2.hconcat([p3, p4])
p12 = cv2.hconcat([p1, p2])
result = cv2.vconcat([p34, p12])

# print
print(p34.shape)
cv2.imshow("Display", result)
cv2.waitKey(0)
