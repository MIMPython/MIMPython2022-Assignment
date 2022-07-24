passage = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
#a)
print('Python' in passage)
print('contain' in passage)
print('experience' in passage)
print('difficult' in passage)

#b)
print(passage.count('Python'))

#c)

words = 1
for i in range(len(passage)):
    if(passage[i] == " "):
        words += 1

print(words)

#d)
for i in range(len(passage)):
    if(passage[i] == "."):
        print(passage[0:i].upper())
        break

