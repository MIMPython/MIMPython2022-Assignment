stg = "python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
checks = ["Python", "contains", "experience", "difficult"]
for check in checks:
    if stg.count(check) != 0 : print("Co xuat hien ",check) 
    else: print("Khong xuat hien",check)

print("So lan 'Python' xuat hien la", stg.count("Python"))

print("Doan van tren co so tu la" , stg.count(" ")+1)

print(stg.capitalize())