import string

paragraph = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you\'ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'
# print(paragraph)

# Phan a)
def preprocess (paragraph):
    paragraph = paragraph.lower() 
    # loai bo dau cau
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation)) 
    # tach cac tu thanh list
    paragraph_splited = paragraph.split(' ') 
    return paragraph_splited

def is_existed(word, paragraph):
    # chuyen tu khoa va doan van thanh chu thuong de giam truong hop
    word = word.lower()
    paragraph_splited = preprocess(paragraph)
    # print(paragraph_splited)
    return word in paragraph_splited

print('Từ khóa "Python" có tồn tại trong đoạn văn trên không:',
      is_existed('Python', paragraph)) # True
print('-' * 30)
print('Từ khóa "contains" có tồn tại trong đoạn văn trên không:',
      is_existed('contain', paragraph)) # False
print('-' * 30)
print('Từ khóa "experience" có tồn tại trong đoạn văn trên không:',
      is_existed('experience', paragraph)) # True
print('-' * 30)
print('Từ khóa "difficult" có tồn tại trong đoạn văn trên không:',
      is_existed('difficult', paragraph)) # False
print('-' * 30)

# Phan b)
def count_word(word, paragraph):
    # chuyen tu khoa va doan van thanh chu thuong de giam truong hop
    word = word.lower()
    paragraph_splited = preprocess(paragraph)
    return paragraph_splited.count(word)

print('Số lần "Python" xuất hiện trong đoạn văn:', count_word('Python', paragraph)) # 5

# Phan c)
print('Số từ trong đoạn văn là:', len(preprocess(paragraph))) # 78

# Phan d)
first_sentence, the_rest = paragraph.split('.', maxsplit=1)
new_paragraph = first_sentence.upper() + '.' + the_rest
print(new_paragraph)
# PYTHON WAS DESIGNED TO BE EASY TO UNDERSTAND AND FUN TO USE (ITS NAME CAME FROM MONTY PYTHON SO A LOT OF ITS BEGINNER TUTORIALS REFERENCE IT). Fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
