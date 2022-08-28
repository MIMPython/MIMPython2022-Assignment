
from PIL import Image

image = Image.open('C:\\Users\\PC\\Desktop\\SD_mooncake.png')
image.show()

print (image.size) # 505, 498

an = image.crop((0,0,249,251))
banh = image.crop((251,0,498,251))
kieng = image.crop((0,252,249,505))
trungthu = image.crop((249,252,498,505))

result = Image.new('RGB', (505,498))
result.paste(banh, (0,0))
result.paste(trungthu, (249,0))
result.paste(an, (0,249))
result.paste(kieng, (249,252))

result.show()

result.save('C:\\Users\\PC\\Desktop\\result.png')