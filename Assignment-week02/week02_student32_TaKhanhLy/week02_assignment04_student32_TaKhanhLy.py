chars = str("Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.")

#(a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?
if 'Python' in chars:
    print('Python is exist')
if 'contains' in chars:
    print('contains is exist')
if 'experience' in chars:
    print('experience is exist')
if 'difficult' in chars:
    print('dissicult is exist')

#(b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
print(chars.count('Python'))
#(c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
chars.split() #The split() method splits a string into a list.
count = len(chars)
print(count)
#(d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.
print(chars.title())