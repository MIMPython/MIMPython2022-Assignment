

#The method used to find if str2 include str1
#Return true if str1 in str2 and return false if str1 not in str2
def FindingWord(str1, str2):
   return str1 in str2

#The method used to count appearances of str1 in str2
def CountKeyword(str1, str2):
    return str2.count(str1)

#The method return the total word of str1
def CountWord(str1):
    word = 1
    for i in range(len(str1)):
        if(str1[i]==' '):
            word += 1
    return word
 

str1 = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). 
Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

str1 = str1.strip(' \t\n\r')
#a)  Results
# Python is in paragraph
# contain is not in paragraph
# experience is in paragraph
# difficulty is not in paragraph 
str = ["Python","contain","experience","difficulty"]
for i in range(len(str)):
    if(FindingWord(str[i], str1)):
        print(str[i] + " is in paragraph") 
    else:
        print(str[i] + " is not in paragraph")


#b)  Keyword "Python" appears 5 times in the paragrahp
print("Keyword Python is appears: ", CountKeyword("Python",str1), "times")



#c) Total word: 78
print('Total word of this paragraph is ', CountWord(str1))
 

#d) Capitalizing the first sentence
str2 = """Python was designed to be easy to understand and fun to use its name came from Monty Python so a lot of its beginner tutorials reference it)."""
str3 = """Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

print(str2.upper() + str3)


    