text = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
print("a) ")
check = ["Python", "contains", "experience", "difficult"]
for i in check:
    a = i in text
    if a == True:
        print(f"{i} có xuất hiện trong đoạn văn")
    else:
        print(f"{i} không xuất hiện trong đoạn văn")
print("b) ")
split = text.split()
print(f"Số lần từ khóa Python xuất hiện trong đoạn văn là {split.count('Python')}")
print("c) ")
print(f"Số từ xuất hiện trong đoạn văn là {len(split)}")
print("d) ")