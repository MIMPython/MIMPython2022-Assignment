letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encoding(word, rot_number):
    password = ""
    for char in word:
        password += letters[(letters.index(char.upper()) + rot_number) % 26]
    return password

def decoding(word, rot_number):
    password = ""
    for char in word:
        password += letters[(letters.index(char.upper()) - rot_number) % 26]
    return password


print(encoding("PYTHON", 13))   # CLGUBA
print(decoding("LUATTRAN", 13))   # YHNGGENA
print(encoding("ABC",13)) #NOP