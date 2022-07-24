string = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
list = string.split(" ")
print(list)

#câu a
wordList = ['Python', 'contains', 'experience', 'difficult']
for word in wordList:
    wordExists = False
    for element in list:
        if element == word:
            wordExists = True
    print("the word '" + word + "' exists in the text: " + str(wordExists))   

#câu b
countPythonWord = 0
for element in list:
    if element == "Python":
        countPythonWord += 1

print("Python word appears in " + str(countPythonWord) + " times")     

#câu c
countWord = 0
for element in list:
    countWord += 1

print ("the text has " + str(countWord) + " words")

#câu d
for element in list:
    print(element.title(), end = " ")
