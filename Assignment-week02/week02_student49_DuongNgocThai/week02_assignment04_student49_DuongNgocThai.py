#Bài 4
str1 = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

#a)
def kiemtra(key_word, str1):
    if key_word in str1 :
        return "Tồn tại"
    else:
        return "Không tồn tại"

print(kiemtra("Python", str1)) #tồn tại
print(kiemtra("contains", str1)) #Không tồn tại
print(kiemtra("experience", str1)) #tồn tại
print(kiemtra("difficult", str1)) #Không tồn tại

#b)
print(str1.count("Python")) #5

#c) 
so_tu = 1
for i in range(len(str1)):
    if i in range(len(str1)):
        so_tu = so_tu + 1
print(so_tu) # 465

#d)
str2 = str1[0:str1.index(".")].title()
str3 = str1[str1.index("."):len(str1)]
print(str2 + str3)