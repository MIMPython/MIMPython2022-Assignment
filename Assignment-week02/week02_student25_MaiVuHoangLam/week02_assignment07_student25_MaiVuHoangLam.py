letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(message):
    result = ""
    for char in message:
        if char != " ":
            result += letter[(letter.index(char.upper()) + 13) % 26]
        else:
            result += " "
    return result


def decrypt(message):
    result = ""
    for char in message:
        if char != " ":
            result += letter[(letter.index(char.upper()) - 13) % 26]
        else:
            result += " "
    return result


print(decrypt("PYTHON FOR NEWBIE"))   # CLGUBA SBE ARJOVR