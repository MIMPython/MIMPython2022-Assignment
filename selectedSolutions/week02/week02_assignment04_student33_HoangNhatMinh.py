import re

checkString = "Python was designed to be easy to understand and fun to use\
     (its name came from Monty Python so a lot of its beginner tutorials reference it).\
     fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python,\
     many find coding in Python a satisfying experience.\
     thus, Python has gained popularity for being a beginner-friendly language, \
     and it has replaced Java as the most popular introductory language at Top U.S. Universities."

# a.
print ("Do \"Python\" exist in the checkString? " + str(checkString.find("Python") != -1)) # True
print ("Do \"Python\" exist in the checkString? " + str(checkString.find("contains") != -1)) # False
print ("Do \"Python\" exist in the checkString? " + str(checkString.find("experience") != -1)) # True
print ("Do \"Python\" exist in the checkString? " + str(checkString.find("difficult") != -1)) # False

# b.
print ("Found " + str(checkString.count("Python")) + " \"Python\" String") # 5

# c.
def countWord(word: str, checkString: str) : 
    regex = "^" + word + "\W|\W" + word + "\W"
    return len(findall(regex, checkString))

print (countWord("Python", checkString))    # 5
print (countWord("to", checkString))        # 4
print (countWord("To", checkString))        # 0
print (countWord("Top", checkString))       # 1

# d.
# tìm vị trí của các dấu chấm
matchers = []
regex1 = "[^A-Z]\. ?.?"
matchers = re.findall(regex1, checkString)

for matcher in matchers :
    if len(matcher) == 4 : 
        tmp = ''
        tmp = tmp + matcher[0:3]
        tmp = tmp + str.upper(matcher[3])
        checkString = checkString.replace(matcher, tmp)
        
print(checkString)

