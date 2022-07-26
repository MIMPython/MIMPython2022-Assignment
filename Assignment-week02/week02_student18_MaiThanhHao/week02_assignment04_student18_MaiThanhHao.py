para = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
para1 = para.split(" ")

# (a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?
words = ['Python', 'contains', 'experience', 'difficult']
for i in range(len(words)):
    if words[i] in para1:
        print("có tồn tại")
    else:
        print("ko tồn tại")
    
#(b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
print(f"\nSố lần xuất hiện của Python: ")
print(para1.count("Python"))

#(c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
print("Số từ của đoạn văn là: ")
print(len(para1))

#(d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.

new_para = ''
for i in para1:
    new_para += ' ' + i.title()
print(new_para)