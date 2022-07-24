paragraph ="""Python was designed to be easy to understand and fun to use (its name came from Monty 
Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you\'ll 
be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying 
experience. Thus, Python has gained popularity for being a beginner-friendly language, 
and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

def a():
    words = ["Python", "contains", "experience", "difficult"]
    for word in words:
        print(word +" in: " + str(paragraph.find(word)!=-1))

def b():
    print("Number \"Python\" in paragaph is: "+str(paragraph.count("Python"))+" times")

def c():
    listParagaph = paragraph.split()
    print("Number word in paragraph is: "+str(len(listParagaph)))

def d():
    listParagaph = paragraph.split(" ")
    answer = listParagaph[0].capitalize()+" "
    for i in range (1, len(listParagaph)):
        if listParagaph[i-1].find(".")!=-1:
            answer+=listParagaph[i].capitalize()
        else: 
            answer+=listParagaph[i]+" "
    print(answer)
if __name__ == '__main__':
    print("a) \n->Answer: ")
    a()
    print()

    print("b) \n->Answer: ")
    b()

    print("c) \n->Answer: ")
    c()
    print()
    
    print("d) \n->Answer: ")
    d()
    
