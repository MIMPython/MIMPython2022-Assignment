paragraph = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). 
Fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

# a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không
print("Python" in paragraph)
print("contains" in paragraph)
print("experience" in paragraph)
print("difficult" in paragraph)

# b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn
print(paragraph.count("Python"))

# c) Tính số từ trong đoạn văn
count = 1
for i in range(len(paragraph)):
    if paragraph[i] == ' ':
        count += 1
print("Total words:", count)

# d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.
firstSentence = paragraph[0:paragraph.find(".")].upper()
paragraph = firstSentence + paragraph[paragraph.find("."):]
print(paragraph)
