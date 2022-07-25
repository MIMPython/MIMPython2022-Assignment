#Bài4
str = """
Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
"""
#a
print("(a) Kiểm tra từ khóa có tồn tại trong đoạn vặn không?")
str1 = ["Python","contains","experience","difficult"]
for i in range(len(str1)):
    if str1[i] in str:
        print( str1[i] + " có trong đoạn văn")
    else: 
        print(str1[i] + " không có trong đoạn văn")
#b
print("(b) Số lần xuất hiện của từ 'Python' là: ",str.count("Python"))
#c
NumOfWord = 1
for i in range(len(str)):
    if(str[i] == ' '):
        NumOfWord += 1
print("(c) Số từ có trong đoạn văn trên là: ", NumOfWord )
#d
print("(d)")
str2 = "Python was designed to be easy to understand and fun to use (its name came from Monty Python"
str3 = str2.upper()
print(str3)

