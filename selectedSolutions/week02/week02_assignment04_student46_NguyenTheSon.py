
#Bài 4:
passage = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it).
Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
"""
#a)
key_words = ['Python', 'contains', 'experience', 'difficult']
for word in key_words:
    if word in passage:
        print(f"Key word '{word}' has existed.")
    else:
        print(f"Key word '{word}' has not existed.")

#b)
print(f"Count the number of key word 'Python' is {passage.count('Python')}")

#c)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z','w']
count = 0
for word in range(len(passage) - 1):
    if passage[word].lower() not in alphabet and passage[word + 1].lower() in alphabet : #kí tự trc không phải chữ và kí tự ngay sau là 1 chữ thì tính là đoạn văn có thêm 1 từ 
        count += 1
print(f"The number of word in the passage is {count + 1}") # +1 vì tính thêm từ đầu tiên
# d)
new_passage = ''
for i in range(passage.find('.')):         #Viết hoa tất cả chữ cái trong câu đầu 
    new_passage += passage[i].upper() 
     
for i in range(passage.find('.'), len(passage)):
    new_passage += passage[i]
print(new_passage)




