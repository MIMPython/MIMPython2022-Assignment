a = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
#a
if "Python" in a:
	print("yes")
else: print("no")

if "contains" in a:
	print("yes")
else: print("no")

if "experience" in a:
	print("yes")
else: print("no")

if "difficult" in a:
	print("yes")
else: print("no")

#b
def count(word, arr):
    n=0
    for x in arr:
        if x == word:
            n += 1
    return n
w = a.split()
print(count('Python', w))

#c
words = a.split()
print(len(words))

#d
print(a.capitalize())