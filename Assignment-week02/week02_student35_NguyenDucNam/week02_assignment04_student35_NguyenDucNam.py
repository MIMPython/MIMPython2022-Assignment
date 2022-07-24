from itertools import count


paragraph = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

def isExist(word): #Kiểm tra từ khóa có tồn tại.
    if word in paragraph:
        print(f"Từ {word} có tồn tại trong đoạn")
    else:
        print(f"Từ {word} không tồn tại trong đoạn")

def countKey(key): #Đếm số lần xuất hiện từ khóa
    print(f"Số lần xuất hiện từ {key} là: {paragraph.count(key)}")

def countWord(): #Đếm số từ có trong đoạn văn
    word = paragraph.split()
    print(f"Số từ trong đoạn văn là: {len(word)}")

def refreshParagraph(): #Viết lại đoạn văn trong đó viết hoa chữ cái đầu của mỗi từ trong câu đầu.
    temp = paragraph.find('.')
    newSentence = paragraph[:temp+1].upper()
    newParagraph = newSentence + paragraph[temp+1:]
    return newParagraph

def main():
        #Câu a
        print("Câu a:")
        isExist('Python')
        isExist('contains')
        isExist('experience')
        isExist('difficult')
        #Câu b
        print(f"\nCâu b:")
        countKey('Python')
        #Câu c
        print(f"\nCâu c:")
        countWord()
        #Câu d
        print(f"\nCâu d:")
        print(refreshParagraph())

if __name__ == '__main__':
            main()