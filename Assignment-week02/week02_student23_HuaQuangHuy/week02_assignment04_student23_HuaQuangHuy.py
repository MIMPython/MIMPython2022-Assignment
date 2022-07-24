# Bài tập 4
# hàm kiểm tra tồn tại
from itertools import count
from re import sub


def checkExist(word, paragraph):
    if word in paragraph:
        print(word + ' xuất hiện')
    else:
        print(word + ' Không xuất hiện')


def countWord(paragraph):
    paragraph.strip()
    while "  " in paragraph:
        paragraph = paragraph.replace("  ", " ")
    numberSpace = paragraph.count(" ")
    return numberSpace + 1


if __name__ == '__main__':
    paragraph = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'

    # a, Kiểm tra xem các từ dưới có trong đoạn văn hay không
    checkExist('Python', paragraph)
    checkExist('contains', paragraph)
    checkExist('experience', paragraph)
    checkExist('difficult', paragraph)

    # b, tính số lần xuất hiện của từ Python trong đoạn văn
    occurrences = paragraph.count('Python')
    print('Số lần xuất hiện từ Python: ' + str(occurrences))

    # c, Đếm số từ trong đoạn văn
    # dựa theo đếm dấu cách (có thể sẽ chưa chuẩn lắm đối với một số trường hợp đặc biệt)
    print('Số từ trong đoạn văn là : ' + str(countWord(paragraph)))

    # d, viết lại đoạn văn với câu đầu viết hoa
    indexOfFirstDot = paragraph.find(".")
    substring = paragraph[0:indexOfFirstDot]
    newSubstring = substring.upper()
    paragraph = paragraph.replace(substring, newSubstring, 1)
    print(paragraph)
