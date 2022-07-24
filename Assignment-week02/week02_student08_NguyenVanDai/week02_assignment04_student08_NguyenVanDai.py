doan_van = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'
#a
pythons=doan_van.count('Python')
contain=doan_van.count('contains')
experience=doan_van.count('experience')
difficult=doan_van.count('difficult')
if (pythons>0):
    print('từ khóa python tồn tại ')
if(contain>0):
    print('từ khóa contain tồn tại')
if(experience>0):
    print('từ khóa experience tồn tại')
if(difficult>0):
    print('từ khóa difficult tồn tại ')
#b
pythons=doan_van.count('Python')
print(pythons)
#c
so_tu=1
for i in range(len(doan_van)):
    if(doan_van[i]==' '):
        so_tu+=1
print(so_tu)
#d
import string
newdoanvan = string.capwords('Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.')
print(newdoanvan)

