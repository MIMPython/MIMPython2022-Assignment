from operator import contains

sentence = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'

#Python, contains, experience, difficult

#a
python = "Python" in sentence
if python:
    print("'Python' co ton tai trong doan van")
else:
    print("'Python' khong ton tai trong doan van")
contains = "contains" in sentence
if contains:
    print("'contains' co ton tai trong doan van")
else:
    print("'contains' khong ton tai trong doan van")
experience = "experience" in sentence
if experience:
    print("'experience' co ton tai trong doan van")
else:
    print("'experience' khong ton tai trong doan van")
difficult = "difficult" in sentence
if difficult:
    print("'difficult' co ton tai trong doan van")
else:
    print("'difficult' khong ton tai trong doan van")
print()

#b
Pythoon_count = sentence.count("Python") 
print(f"Số lần xuất hiện của từ khoá Python là {Pythoon_count} lần")
print()

#c
words = sentence.split(" ")
number_of_hyphen = len(sentence.split("-"))
print(f"Số từ của câu đã cho là: {len(words) + number_of_hyphen - 1}")
print()

#d
sentence_remake = sentence.title()
print(f"Viết hoa các từ trong câu: \n{sentence_remake}")