text = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
#a)
print("a)")
keyword_check = ["Python", "contains", "experience", "difficult"]
for i in keyword_check:
    a = i in text
    if a == True:
        print(f"{i} có xuất hiện trong đoạn văn")
    else:
        print(f"{i} không xuất hiện trong đoạn văn")
#b)
print("b)")
text_splitted = text.split()
text_splitted.count("Python")
print(f"Số lần từ khóa Python xuất hiện trong đoạn văn là {text_splitted.count('Python')}")

#c)
print("c)")
print(f"Số từ xuất hiện trong đoạn văn trên là {len(text_splitted)}")

#d)
print("d)")
full_stop = text_splitted.index("it).")
text_rewrited = ""
text_splitted_rewrited = []
for i in range(0, full_stop + 1):
    j = text_splitted[i].title()
    text_splitted_rewrited.append(f"{j} ")
for i in range(full_stop + 1, len(text_splitted)):
    j = text_splitted[i]
    text_splitted_rewrited.append(f"{j} ")
for i in text_splitted_rewrited:
    text_rewrited += i
print(text_rewrited)



