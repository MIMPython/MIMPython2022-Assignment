
text = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'

def a():
    if 'Python' in text:
        print ('true')
    else:
        print ('false')

    if 'contains' in text:
        print ('true')
    else:
        print ('false')

    if 'expereince' in text:
        print ('true')
    else:
        print ('false')

    if 'difficult' in text:
        print ('true')
    else:
        print ('false')

a()

def b():
    result = text.count('Python')
    print ('so lan xuat hien tu Python: ' + str(result))
b()

def c():
    list = text.split()
    result = len(list)
    print ('so tu = ' + str(result))

c()

