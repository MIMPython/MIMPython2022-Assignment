py = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'
print('Python' in py)
print('contains' in py)
print('experience' in py)
print('difficult' in py )
print(py.find('Python'))

so_tu=1
for i in range(len(py)):
    if(py[i]==' '):
        so_tu=so_tu+1
print("Total words: ",so_tu)

import string
string.capwords(py)
