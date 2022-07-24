alphabet = 'abcdefghijklmnopqrstuvwxyz'
def encode(word):
    result = ''
    for i in range(len(word) - 1):
        for j in range(len(alphabet) - 1):
            if word[i]==alphabet[j]:
                result += alphabet[j-13]

    return result 
word = str(input('Enter your word\n'))
word.encode()


def decode(word):
    result = ''
    for i in range(len(word) - 1):
        for j in range(len(alphabet) - 1):
            if word[i]==alphabet[j]:
                result += alphabet[j+13-26]
    return result
code = str(input('Enter your code\n'))
code.decode()


