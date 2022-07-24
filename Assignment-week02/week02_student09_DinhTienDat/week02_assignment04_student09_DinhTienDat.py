str = """
Python was designed to be easy to understand and fun to use 
(its name came from Monty Python so a lot of its beginner 
tutorials reference it). Fun is a great motivator, and since 
you’ll be able to build prototypes and tools quickly with Python, 
many find coding in Python a satisfying experience. Thus, Python 
has gained popularity for being a beginner-friendly language, and 
it has replaced Java as the most popular introductory language at 
Top U.S. Universities.
"""
#Câu a,b)
print("Cho đoạn văn:")
print(str)

print("Nhập từ mà bạn muốn kiểm tra vào đây:")
sub = input()
result = str.count(sub)

if result >0:
	print("Từ khoá",sub,"tồn tại trong đoạn văn và xuất hiện",result,"lần")
else:
	print("Từ khoá",sub,"không xuất hiện trong đoạn văn")

#Câu c

so_tu=1

for i in range(len(str)):
    if(str[i]==' '):
        so_tu=so_tu+1
print("Hơn nữa, tổng số từ có trong đoạn văn là: ",so_tu)

#Câu d:
print("Bạn có muốn viết hoa các từ của đoạn văn gốc không?")

yeu_cau = input()

if yeu_cau == "co":
	print(str.title())
elif yeu_cau == "khong":
	print("hoi z, pai nha ^^")
else:
	print("Yêu cầu nhập không đúng.")

