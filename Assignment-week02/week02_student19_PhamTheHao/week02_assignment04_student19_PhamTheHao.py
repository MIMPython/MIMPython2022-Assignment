"""
Bài tập 4. Cho đoạn văn sau
Python was designed to be easy to understand and fun to use (its name came 
from Monty Python so a lot of its beginner tutorials reference it). Fun is 
a great motivator, and since you'll be able to build prototypes and tools 
quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, 
and it has replaced Java as the most popular introductory language at 
Top U.S. Universities.
"""
import os
paragraph = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
"""
(a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn 
    tại trong đoạn văn trên hay không?
"""
print('(a)')
print("Python" in paragraph)
print("contains" in paragraph)
print("experience" in paragraph)
print("difficult" in paragraph)
os.system("pause")

"""
(b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
"""
print('(b)')
count = paragraph.count("Python")
print(f"Từ khóa 'Python' xuất hiện {count} lần trong đoạn văn.")
os.system("pause")

"""
(c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái 
    (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
"""
print('(c)')
#Cách 1:
list_of_words = paragraph.split()
print(f"Trong đoạn văn trên có {len(list_of_words)} từ.")

#Cách 2:
count_word = 0
for char in paragraph:
    if char == ' ':
        count_word += 1
print(f"Trong đoạn văn trên có {count_word + 1} từ.")
os.system("pause")

"""
(d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu 
tiên của đoạn văn.
"""
print('(d)')
new_paragraph = paragraph.title()
print(new_paragraph)