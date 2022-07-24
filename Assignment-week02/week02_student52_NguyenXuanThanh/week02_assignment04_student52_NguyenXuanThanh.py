# Bài tập 4. Cho đoạn văn sau
# Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner 
# tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with 
# Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly 
# language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.

# (a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?
# (b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
# (c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
# (d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.

str1 = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

#a) 
#Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không : 
print("Python" in str1) # True
print("contains" in str1) # True
print("experience" in str1) # True
print("difficult" in str1) # True
#b)
str1 = str1.replace(",","")
str1 = str1.replace(".","")
str1 = str1.replace("(","")
str1 = str1.replace(")","")
str1 = str1.split(" ")
def countKey(str,key):
    temp = 0 
    i = 0 
    while(i < len(str)):
        if(str[i] == key):
            temp +=1
        i+=1  
    return temp
#Số lần xuất hiện của từ khóa Python trong đoạn văn là : 
print(countKey(str1,'Python')) #5
#c)
#Số từ trong đoạn văn trên
print(len(str1)) #78
#d) 




