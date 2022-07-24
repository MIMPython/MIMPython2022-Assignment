str='Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'
n=str.find('Python')
j=len(str)
if n!=-1 :
    print('YES')
else: 
    print ("NO")
    
s=str.replace('Python','')
print(int((len(str)-len(s))/6))
print(len(str)-len(str.replace(' ',''))+1)

k="p"
for i in str:
    if k==" ":
        print(i.upper(),end="")
    else:
        print(i,end="")
    k=i
#print(capwords(str))

       
