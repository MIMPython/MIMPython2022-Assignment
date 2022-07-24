#(1) 
print("(1)")
for i in range(1,7):
    print ("*"*i)

#(2) 
print("(2)")
for i in range(6,0,-1):
    print("*"*i) 

#(3)
print("(3)")
print("*"*6)
for i in range(6,2,-1):
    print("*"+" "*(i-1-2)+"*")
print("*")

#(4)
print("(4)")
def veDauSao(x):
    str=""
    for i in range(1,2*x):
        if (i%2==0):
            str=str+" "
        else:
            str=str+"*"
    return str

for i in range(1,7):
    print(" "*(6-i)+veDauSao(i)+" "*(6-i))

#5
print("(5)")
for i in range(6,0,-1):
    print(" "*(6-i)+veDauSao(i)+" "*(6-i))

#6
print("(6)")
print(" "*5+"*"+" "*5)
for i in range(4,0,-1):
    print(" "*i+"*"+" "*(11-i*2-2)+"*"+" "*i)

print(veDauSao(6))

