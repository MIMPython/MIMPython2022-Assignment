def checkString(string: str, paragraph:str):
    if string in paragraph:
        return f"{string} tồn tại trong đoạn văn"
    else:
        return f"{string} không tồn tại trong đoạn văn"

def countString(string : str, paragraph:str):
    count = 0
    for p in paragraph.split():
        if p == string:
            count = count + 1
    return f"Số lần xuất hiện của {string} là  {count}"

def countEnglish(paragraph:str):
    count = 0
    for p in paragraph.split(" "):
        count = count+1
    return f"Số từ tiếng Anh là: {count}"

def uppcaseFirst(paragraph:str):
    for p in paragraph.split("."):
        return p.upper()

if __name__ == '__main__':
    paragraph = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

    #a
    print(checkString("Python",paragraph))
    #Python tồn tại trong đoạn văn

    print(checkString("contains",paragraph))
    #contains không tồn tại trong đoạn văn

    print(checkString("experience",paragraph))
    #experience tồn tại trong đoạn văn

    print(checkString("difficult",paragraph))
    #difficult không tồn tại trong đoạn văn

    #b
    print(countString("Python",paragraph))
    #Số lần xuất hiện của Python là  4

    #c
    print(countEnglish(paragraph))
    #Số từ tiếng Anh là: 78

    #d
    print(uppcaseFirst(paragraph))
    #PYTHON WAS DESIGNED TO BE EASY TO UNDERSTAND AND FUN TO USE (ITS NAME CAME FROM MONTY PYTHON SO A LOT OF ITS BEGINNER TUTORIALS REFERENCE IT)
