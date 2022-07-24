inputString = '''Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it).
Fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities'''

def checkIfASubstringInInputString(substring, inputString) :
    return substring in inputString

def countSubstringInInputString(substring, inputString):
    return inputString.count(substring)

def countWordsInInputString(inputString):
    return inputString.count(" ") - 1

def upperInputString(inputString):
    return inputString.upper()

print(checkIfASubstringInInputString("Python", inputString))
print(countSubstringInInputString("Python", inputString))
print(countWordsInInputString(inputString))
print(upperInputString(inputString))