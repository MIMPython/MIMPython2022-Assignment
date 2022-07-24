para = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
#phần a:
print("Python" in para) #True
print("contains" in para) #False
print("experience" in para) #True
print("difficult" in para) #False

#phần b:
para1= para.replace(',','')
para2 = para1.split(" ")

count={}
for word in para2:
    if word == 'Python':
        if word in count:
            count[word] += 1
        else:
            count[word] =1

print(count) #Python: 5

#phần c:
para3=para1.replace('-',' ')
para4= para3.replace('.',' ')
para5= para4.split(" ")
count=0
for word in para5:
    if word == '':
        count += 1
print(len(para5)-count) #80

#phần d:
para6=para.split(".")
para6[0]=para6[0].upper()
para6.pop(len(para6)-1)
print(para6)
new_para = ""
for para in para6:
    new_para += para +"."

print(new_para)
