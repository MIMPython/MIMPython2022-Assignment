print("Bài 4: Cho đoạn văn sau:")
doanvan = """
Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials 
reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find 
coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has 
replaced Java as the most popular introductory language at Top U.S. Universities.
"""

print("a) Kiểm tra các từ khóa có tồn tại trong văn bản không?")
a = "Python" in doanvan
if a == True:
    print("Từ khóa 'Python' có tồn tại")
else:
    print("Từ khóa 'Python' không tòn tại")

b = "contains" in doanvan    
if b == True:
    print("Từ khóa 'contains' có tồn tại")
else:
    print("Từ khóa 'contains' không tòn tại")

c = "experience" in doanvan    
if c == True:
    print("Từ khóa 'experience' có tồn tại")
else:
    print("Từ khóa 'experience' không tòn tại")

d = "difficult" in doanvan
if d == True:
    print("Từ khóa 'difficult' có tồn tại")
else:
    print("Từ khóa 'difficult' không tòn tại")

print()
print("b) Đếm số lần xuất hiện từ khóa 'Python' trong đoạn văn")
lst = doanvan.split()
d = doanvan.count("Python")
print("Số lần xuất hiện từ khóa 'Python' trong đoạn văn là:", d)

print()
print("c) Tính số từ xuất hiện trong đoạn văn trên")
dem = 0
for j in lst:
    dem += 1
print("Số từ trong đoạn văn trên là:", dem)

print()
print("d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn:")
doan = """ 
Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). 
"""
l = ""
van = doan.split()
for k in van:
    k = k.upper()
    l = l + k + " "
l.strip()
print(l)