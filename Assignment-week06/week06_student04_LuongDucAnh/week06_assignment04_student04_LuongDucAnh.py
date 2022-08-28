from PIL import Image

im = Image.open("C:/Users/imlda/Desktop/week06_student04_LuongDucAnh/additionalFolder/SD_mooncake.png")
width, height = im.size

#Crop ảnh
im1 = im.crop((width/2, 0, width - 2, height/2)) 
im2 = im.crop((width/2, height/2, width - 2, height))
im3 = im.crop((1, 0, width/2, height/2))
im4 = im.crop((1, height/2, width/2, height))

result = Image.new("RGB", (im1.width + im4.width, im1.height + im4.height))
result.paste(im1, (0, 0))
result.paste(im2, (im1.width, 0))
result.paste(im3, (0, im1.height + 1))
result.paste(im4, (im1.width, im1.height + 1))

result.show()
result.save("./additionalFolder/result.png")