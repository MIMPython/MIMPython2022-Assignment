# Bài tập 4. Cho đoạn văn sau
def words_exist(s):
    if "Python" in s:
        print("Python is existed in s")
    else:
        print("Python is not existed in s")
    if "contains" in s:
        print("contains is existed in s")
    else:
        print("contains is not existed in s")
    if "experience" in s:
        print("experience is existed in s")
    else:
        print("experience is not existed in s")
    if "difficult" in s:
        print("difficult is existed in s")
    else:
        print("difficult is not existed in s")
# (b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
def count_words(s):
    return s.count("Python")
# (c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
def worded(s):
    return len(s.split(' '))
# (d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.
def upper_case_first_character(s):
    return s.title()
if __name__ == "__main__":
    s = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
    words_exist(s) # Python is existed in s. contains is not existed in s. experience is existed in s. difficult is not existed in s
    print(count_words(s)) # 5
    print(worded(s)) # 78
    print(upper_case_first_character(s)) # Python Was Designed To Be Easy To Understand And Fun To Use (Its Name Came From Monty Python So A Lot Of Its Beginner Tutorials Reference It). Fun Is A Great Motivator, And Since You’Ll Be Able To Build Prototypes And Tools Quickly With Python, Many Find Coding In Python A Satisfying Experience. Thus, Python Has Gained Popularity For Being A Beginner-Friendly Language, And It Has Replaced Java As The Most Popular Introductory Language At Top U.S. Universities.



