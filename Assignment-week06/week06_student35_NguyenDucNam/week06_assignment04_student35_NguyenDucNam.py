from PIL import Image

photos = Image.open('C:/Users/namyh/Desktop/New folder/additionalFolder/SD_mooncake.png')
x,y = photos.size

p1 = photos.crop((x/2,0,x,y/2))
p2 = photos.crop((x/2,y/2,x,y))
p3 = photos.crop((0,0,x/2,y/2))
p4 = photos.crop((0,y/2,x/2,y))
newPhotos = Image.new('RGB',(x,y))
newPhotos.paste(p1,(0,0))
newPhotos.paste(p2,(int(x/2),0))
newPhotos.paste(p3,(0,int(y/2)))
newPhotos.paste(p4,(int(x/2),int(y/2)))
newPhotos.save('./additionalFolder/result.png')