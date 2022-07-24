s = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
# Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn
print("Python" in s)
print("contains" in s)
print("experience" in s)
print("difficult" in s)

# Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
print(s.count('Python'))

# Tính số từ trong đoạn văn
words = s.split()
print(len(words))

#Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn
sentences = s.split('.')
print(s.replace(sentences[0],sentences[0].upper()))