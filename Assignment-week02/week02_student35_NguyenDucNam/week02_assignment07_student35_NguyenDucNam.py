def encode(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for char in text:
        if char in alphabet:
            code += alphabet[(alphabet.find(char)+13)%26]
        else:
            code += char
    return code

def decode(text):  
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for char in text:
        if char in alphabet:
            code += alphabet[(alphabet.find(char)-13)%26]
        else:
            code += char
    return code 


print(encode('DUC NAM'))
print(decode('DUC NAM')) 