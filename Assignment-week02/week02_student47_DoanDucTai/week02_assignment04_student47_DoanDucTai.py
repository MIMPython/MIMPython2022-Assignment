#a
print("a)")
paragraph="Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
findPython = paragraph.find("Python")
findContains =  paragraph.find("contains")
findExperience = paragraph.find("experience")
findDiffcult = paragraph.find("difficult")
if (findPython != -1):
    print("Python tồn tại trong đoạn văn")
else: print("Python không tồn tại trong đoạn văn")
if (findContains != -1):
    print("contains tồn tại trong đoạn văn")
else:
    print("contains không tồn tại trong đoạn văn")
if (findExperience != -1):
    print("experience tồn tại trong đoạn văn")
else:
    print("experience không tồn tại trong đoạn văn")
if (findDiffcult != -1):
    print("diffcult tồn tại trong đoạn văn")
else:
        print("diffcult không tồn tại trong đoạn văn")

#b
print("b)")
countOfPython = paragraph.count("Python")
print("Số lần xuất hiện của Python:", countOfPython)

#c
print()
print("c)")
paragraph1 = paragraph
charr = list()
charr = paragraph.split(" ")
for i in range(0,len(charr)) :
    ch = charr[i][0]
    while (ch.isalpha() == False):
        charr[i] = charr[i][1: (len(charr[i]) - 1)]
        ch = charr[i][0]
    ch = charr[i][len(charr[i])-1]
    while (ch.isalpha() == False):
        charr[i] = charr[i][0: (len(charr[i]) - 1)]
        le=len(charr[i])-1
        ch = charr[i][le]
i=0 
while (i < len(charr)):
    for j in range(0, i):
        if (charr[i] ==  charr[j]):
            charr.pop(i)
    i +=1
print("số từ trong đoạn văn trên là", len(charr))

#d
print()
print("d)")
pa=paragraph[0: (paragraph.find("."))]
paragraph1= pa.upper() + paragraph[(paragraph.find(".")) : (len(paragraph)-1)]
print(paragraph1)