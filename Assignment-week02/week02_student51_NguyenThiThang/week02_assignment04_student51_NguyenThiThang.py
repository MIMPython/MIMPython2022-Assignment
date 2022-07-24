str='''Python was designed to be easy to understand and fun 
to use (its name came from Monty Python so a lot of its 
beginner tutorials reference it). Fun is a great motivator, 
and since you’ll be able to build prototypes and tools 
quickly with Python, many find coding in Python a satisfying 
experience. Thus, Python has gained popularity for being a 
beginner-friendly language, and it has replaced Java as the 
most popular introductory language at Top U.S. Universities.'''

#a
if (str.find("Python")<0):
    print("Python khong ton tai trong doan van tren")
else:
    print("Python co ton tai trong doan van tren")

if (str.find("contains")<0):
    print("contains khong ton tai trong doan van tren")
else:
    print("contains co ton tai trong doan van tren")

if (str.find("experience")<0):
    print("experience khong ton tai trong doan van tren")
else:
    print("experience co ton tai trong doan van tren")

if (str.find("difficult")<0):
    print("difficult khong ton tai trong doan van tren")
else:
    print("difficult co ton tai trong doan van tren")

#b
print("So lan xuat hien cua Python la:",str.count("Python"))
#c
print("So tu trong doan van tren la:",str.count(" ")+1)
#d
str1=str[0:str.find(".")]
print(str.replace(str1,str1.title()))

