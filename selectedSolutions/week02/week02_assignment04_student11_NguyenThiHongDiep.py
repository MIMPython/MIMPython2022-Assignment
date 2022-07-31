import string

paragraph = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you\'ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'

def preparation(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation)) # Loại bỏ dấu câu
    paragraphSplit = paragraph.split(' ') # Tách các từ thành list  
    return paragraphSplit

# a
def existed(word, paragraph):
    word = word.lower()
    paragraph_splited = preparation(paragraph)
    
    if (word in paragraph_splited) is True:
        print ('Tu khoa \"', word, '\" ton tai trong doan van tren.')
    else:
        print('Tu khoa \"', word, '\" khong ton tai trong doan van tren.')

if __name__ == '__main__':
    existed('Python', paragraph) # Tu khoa " python " ton tai trong doan van tren.
    existed('contains', paragraph) # Tu khoa " contains " khong ton tai trong doan van tren.
    existed('experience', paragraph) # Tu khoa " experience " ton tai trong doan van tren.
    existed('difficult', paragraph) # Tu khoa " difficult " khong ton tai trong doan van tren.

# b
def count(word, paragraph):
    word = word.lower()
    paragraph_splited = preparation(paragraph)
    return paragraph_splited.count(word)

print('Tu khoa \" Python \" xuat hien', count('Python', paragraph), 'lan trong doan van tren.') # Tu khoa " Python " xuat hien 5 lan trong doan van tren.

# c
print('Co', len(preparation(paragraph)), 'tu trong doan van tren.') # Co 78 tu trong doan van tren.

# d
firstSentence, remainingSentences = paragraph.split('.', maxsplit = 1)
newParagraph = firstSentence.upper() + '.' + remainingSentences
print(newParagraph) # PYTHON WAS DESIGNED TO BE EASY TO UNDERSTAND AND FUN TO USE (ITS NAME CAME FROM MONTY PYTHON SO A LOT OF ITS BEGINNER TUTORIALS REFERENCE IT). Fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.

 