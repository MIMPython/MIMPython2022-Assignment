def rot13Encode(text): #Hàm mã hoá thông điệp ROT-13
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = ""
    for char in text:
        if char in abc:
            code += abc[(abc.find(char)+13)%26]
        elif char in ABC:
            code += ABC[(ABC.find(char)+13)%26]
        else:
            code += char
    return code

def rot13Decode(text): #Hàm giải mã thông điệp ROT-13
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = ""
    for char in text:
        if char in abc:
            code += abc[(abc.find(char)-13)%26]
        elif char in ABC:
            code += ABC[(ABC.find(char)-13)%26]
        else:
            code += char
    return code

print (rot13Encode("Duc Anh")) #Mã hoá thông điệp "Duc Anh" -> Qhp Nau
print (rot13Decode("Clguba")) #Giải mã thông điệp thông điệp "Clguba" -> Python