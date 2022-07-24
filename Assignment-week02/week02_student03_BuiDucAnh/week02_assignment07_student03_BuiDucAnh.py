plainText = input("Nhập vào văn bản muốn mã hóa: ")
shift = 13

def caesar(plainText, shift): 
    cipherText = ""
    for char in plainText:
        if char.isalpha():
            stayInAlphabet = ord(char) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter

    print ("Văn bản được mã hóa: ", cipherText)
    return cipherText

caesar(plainText, shift)