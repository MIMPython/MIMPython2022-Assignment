#Bài 7:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
alphabet_1 = 'abcdefghijklmnopqrstuvwxyz'
def modulo_26(a, b):
    a_modullo_b = a + b
    while a_modullo_b >= 26 :
        a_modullo_b = a + b - 26 
    return a_modullo_b
    

def caesar_0(messages):
    code_caesar = ''
    for message in messages:
        number = modulo_26(alphabet_1.find(message.lower()), 19)
        code_caesar += alphabet[number]
    print(code_caesar)

if __name__ == '__main__':
    caesar_0('Python') #irmahg
    caesar_0('theson') #maxlhg

def caesar_1(messages):
    code_caesar = ''
    for message in messages:
        number = modulo_26(alphabet_1.find(message.lower()), -19)
        code_caesar += alphabet[number]
    print(code_caesar)

if __name__ == '__main__':
    caesar_1('irmahg') #irmahg
    caesar_1('maxlhg') #maxlhg