abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(len(abc))

abc_encryted = abc[:]

for i in range(0,13):
    abc_encryted[i] = abc[i+13]

for i in range(13,26):
    abc_encryted[i] = abc[i-13]

def encrypt(x):
    y = x.upper()
    name = []
    for i in y:
        name.append(i)
    name_encrypted = []
    for i in name:
        j = abc.index(i)
        name_encrypted.append(abc_encryted[j])
    k = ""
    for i in name_encrypted:
        k += i
    print(k)
    
x = str(input("Mã hóa: "))     
encrypt(x)

def decode(x):
    y = x.upper()
    name = []
    for i in y:
        name.append(i)
    name_encrypted = []
    for i in name:
        j = abc_encryted.index(i)
        name_encrypted.append(abc[j])
    k = ""
    for i in name_encrypted:
        k += i
    print(k)
    
x = str(input("Giải mã: "))     
decode(x)

# encrypt(nguyenHoanglong) #ATHLRAUBNATYBAT
# decode(ATHLRAUBNATYBAT) #NGUYENHOANGLONG