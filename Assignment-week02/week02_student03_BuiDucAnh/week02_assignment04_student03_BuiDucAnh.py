from itertools import count


doc = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its 
    beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools 
    quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being 
    a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."""""

#a. Kiểm tra các từ khóa có tồn tại hay không

#Python
if doc.count('Python') > 0:
    print('Có tồn tại từ khóa Python')
else:
    print('Không tồn tại từ khóa Python')

#contains
if doc.count('contains') > 0:
    print('Có tồn tại từ khóa contains')
else:
    print('Không tồn tại từ khóa contains')

#experience
if doc.count('experience') > 0:
    print('Có tồn tại từ khóa experience')
else:
    print('Không tồn tại từ khóa experience')

#difficult
if doc.count('difficult') > 0:
    print('Có tồn tại từ khóa difficult')
else:
    print('Không tồn tại từ khóa difficult')


#b. Số lần xuất hiện từ khóa Python
print(doc.count('Python'))

#c.Đếm số từ trong đoạn
listDoc = doc.split()
print(len(listDoc))

#d. Viết lại đoạn văn
doc1 = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its 
    beginner tutorials reference it).""".title() #Viết hoa tất cả chữ cái trong câu đầu tiên
print(len(doc1)) #Lấy độ dài câu đầu
doc2 = doc[147:] #Lấy đoạn mới bắt đầu từ câu 2
print(doc1 + doc2) #Ghép 2 câu làm đoạn hoàn chỉnh