def is_letter(let):
    return 64 < let < 91


def goc_mahoa(string, ROT):
    string = string.upper()
    res = ''
    for i in range(len(string)):
        letter = ord(string[i])
        if is_letter(letter):
            letter += ROT
            if is_letter(letter):
                res += chr(letter)
            else:
                letter -= 26
                res += chr(letter)
        else:
            res += string[i]

    print(res)


def mahoa_goc(string, ROT):
    string = string.upper()
    res = ''
    for i in range(len(string)):
        letter = ord(string[i])
        if is_letter(letter):
            letter -= ROT
            if is_letter(letter):
                res += chr(letter)
            else:
                letter += 26
                res += chr(letter)
        else:
            res += string[i]

    print(res)


if __name__ == '__main__':
    goc_mahoa('PYTHON', 13)
    mahoa_goc('irmahg', 19)
