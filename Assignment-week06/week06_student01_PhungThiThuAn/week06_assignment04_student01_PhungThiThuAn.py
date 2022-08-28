from PIL import Image
import cv2

# đọc file ảnh
pic = cv2.imread("./additionalFolder/mooncake.jpg")
h, w, d = pic.shape
print(h, w, d)

# +1 để hình cắt đều và đẹp hơn
w_midpoint = int(w/2)+1
h_midpoint = int(h/2)+1

# cắt và lưu ảnh trong additionalFolder
part1 = pic[:h_midpoint, :w_midpoint] # ăn
cv2.imwrite('additionalFolder/part1.jpg', part1)
part2 = pic[h_midpoint:, :w_midpoint] # kiêng
cv2.imwrite('additionalFolder/part2.jpg', part2)
part3 = pic[:h_midpoint, w_midpoint:] # bánh
cv2.imwrite('additionalFolder/part3.jpg', part3)
part4 = pic[h_midpoint:, w_midpoint:] # Trung Thu
cv2.imwrite('additionalFolder/part4.jpg', part4)

path = './additionalFolder/'
im_path_list = [path+'part3.jpg', path+'part4.jpg', path+'part1.jpg', path+'part2.jpg']

new_im = Image.new('RGB', (w, h))
im1 = Image.open(im_path_list[0])
new_im.paste(im1, (0, 0))
im1_h, im1_w = im1.size
new_im.paste(Image.open(im_path_list[1]), (im1_h, 0))
new_im.paste(Image.open(im_path_list[2]), (0, im1_w))
new_im.paste(Image.open(im_path_list[3]), (im1_h, im1_w))

new_im.save(path+'resultMooncake.jpg')
# Output là file result.jpg trong thư mục additionalFolder
# bài làm của mình có tham khảo ở trang https://helpex.vn/question/ket-hop-mot-so-hinh-anh-theo-chieu-ngang-voi-python-5cd00d69ae03f632bc15aced


