paragraph ="""Python was designed to be easy to understand and fun to use (its name came from Monty 
Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you\'ll 
be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying 
experience. Thus, Python has gained popularity for being a beginner-friendly language, 
and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

def a():
    words = ["Python", "contains", "experience", "difficult"]
    for word in words:
        if paragraph.find(word):
            print (word + " exists in paragraph")
        else:
            print (word + " don't exists in paragraph")

def b():
    result = paragraph.count("Python")
    print("'Python' appears in paragaph "+ str(result) +" times")
    
def c():
    listParagraph = paragraph.split()
    print ("The paragraph has " + str(len(listParagraph)) + " words")
    
def d(): 
    new_paragraph = paragraph.title()
    print (new_paragraph)
    
if __name__ == '__main__':
    print("(a) ")
    a()
    print("\n")
    
    print("(b) ")
    b()
    print("\n")
    
    print("(c) ")
    c()
    print("\n")
    
    print("(d) ")
    d()
    print("\n")
    