paragraph = "Python was designed to be easy to understand and fun to use (its \
    name came from Monty Python so a lot of its beginner tutorials reference it). \
        Fun is a great motivator, and since you'll be able to build prototypes \
            and tools quickly with Python, many find coding in Python a satisfying experience. \
                Thus, Python has gained popularity for being a beginner-friendly language, \
                    and it has replaced Java as the most popylar introductory language\
                         at Top U.S. Universities."

# a
print("Python" in paragraph)
print("contains" in paragraph)
print("experience" in paragraph)
print("difficult" in paragraph)

# b
count = 0
keyword = "Python"
for i in range(len(paragraph)):
    if keyword == paragraph[i : (i + len(keyword))]:
        count += 1
print(count)

# c
c = 0
for index in range(len(paragraph)):
    if paragraph[index] == " ":
        c += 1
print("Number of words in paragraph:", c + 1)

# d
for j in range(len(paragraph)):
    if paragraph[j] == ".":
        break
new_paragraph = paragraph[:j].upper() + paragraph[j:]
print(new_paragraph)
