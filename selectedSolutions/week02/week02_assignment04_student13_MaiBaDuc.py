'''
Bài tập 4. Cho đoạn văn sau
Python was designed to be easy to understand and fun to use (its name came from 
Monty Python so a lot of its beginner tutorials reference it). 
Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, 
many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as
the most popular introductory language at Top U.S. Universities.

(a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?
(b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
(c) Một từ (tiếng Anh) là một chuỗi liên tục các chữ cái thuộc bảng chữ cái (tiếng Anh), viết thường hoặc viết hoa. Tính số từ trong đoạn văn trên.
(d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.

'''

sample = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'

def func_a():
    key_words = ['Python', 'contains', 'experience', 'difficult']
    for key_word in key_words:
        if key_word in sample: 
            print("Sample has keyword: " + key_word)
        else:
            print("Sample has not keyword: " + key_word)

def func_b():
    count=0
    for i in sample.split():
        if(i=='Python'):
            count += 1
    print(count)

def func_c():
    count=0
    for i in sample.split():
        count += 1
    print(count)

def func_d():
    pos = sample.find('.')
    sample_1 = sample[:pos].upper()
    sample_2 = sample[pos:]
    print(sample_1 + sample_2)

func_a()
func_b()
func_c()
func_d()