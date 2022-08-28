from PIL import Image


moonCake = Image.open(
    ".\\additionalFolder\\week06_assignment04_student28_MaiThanhLiem_problem.png"
)
moonCake = moonCake.crop((0, 0, 498, 498))
# moonCake.show()

imageWidth = moonCake.size[0]
imageHeight = moonCake.size[1]

an = moonCake.crop((0, 0, imageWidth / 2, imageHeight / 2))
banh = moonCake.crop((imageWidth / 2, 0, imageWidth, imageHeight / 2))
kieng = moonCake.crop((0, imageHeight / 2, imageWidth / 2, imageHeight))
trungthu = moonCake.crop((imageWidth / 2, imageHeight / 2, imageWidth, imageHeight))

newImage = Image.new("RGB", (imageWidth, imageHeight))
newImage.paste(banh, (0, 0, banh.size[0], banh.size[1]))
newImage.paste(trungthu, (banh.size[0], 0, banh.size[0] * 2, banh.size[1]))
newImage.paste(an, (0, banh.size[1], banh.size[0], banh.size[1] * 2))
newImage.paste(kieng, (banh.size[0], banh.size[1], banh.size[0] * 2, banh.size[1] * 2))
newImage.save(
    ".\\additionalFolder\\week06_assignment04_student28_MaiThanhLiem_solution.png"
)
newImage.show()
