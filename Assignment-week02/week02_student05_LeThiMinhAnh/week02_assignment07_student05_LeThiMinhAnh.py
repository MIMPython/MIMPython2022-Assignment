def encodeROT13(inString):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outString = ""
    for i in inString:
        if i in alphabet:
            indexAlpha = alphabet.find(i)
            if indexAlpha <= 12 or indexAlpha >= 26 and indexAlpha <= 38:
                i = alphabet[alphabet.find(i)+13]
            else:
                i = alphabet[alphabet.find(i)-13]
        outString += i
    return outString


def decodeROT13(inString):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outString = ""
    for i in inString:
        if i in alphabet:
            indexAlpha = alphabet.find(i)
            if indexAlpha >= 13 and indexAlpha <= 25 or indexAlpha >= 39 and indexAlpha <= 51:
                i = alphabet[alphabet.find(i)-13]
            else:
                i = alphabet[alphabet.find(i)+13]
        outString += i
    return outString


print(encodeROT13("The quick brown fox jumps over 13 lazy dogs."))
print(decodeROT13("Gur dhvpx oebja sbk whzcf bire 13 ynml qbtf."))
