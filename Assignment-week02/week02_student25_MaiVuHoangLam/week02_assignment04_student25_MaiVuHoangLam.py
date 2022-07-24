paragraph = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so " \
            "a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able " \
            "to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. " \
            "Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as " \
            "the most popular introductory language at Top U.S. Universities"

# 4a)


def check(word):
    if word in paragraph:
        return True
    return False


print(check("Python"))
print(check("contains"))
print(check("experience"))
print(check("difficult"))


# 4b)
def count(word):
    num = paragraph.count(word)
    return num


print(count("Python"))


# 4c)


