text = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
# a,
def checkWord(word):
    check = text.find(str(word))
    if int(check) > -1:
        message = str(word) + " is found"
        print("Message: ", message)
    else:
        print("Not found")
print("a,")
checkWord("Python")
checkWord("contains")
checkWord("experience")
checkWord("difficult")
# b, 
freq = text.count("Python")
print("b,", freq)
# c, 
number = text.count(" ")
print("Number of words is: ", number + 1)        
# d, 
wordList = text.split()
newList = []
for word in wordList:
    header = word[0].upper()
    word = word.replace(word[0], header, 1)
    newList.append(word)
newText = ""
for word in newList:
    newText = str(newText) + str(word) + " "
newText = newText.rstrip()
print(newText)
