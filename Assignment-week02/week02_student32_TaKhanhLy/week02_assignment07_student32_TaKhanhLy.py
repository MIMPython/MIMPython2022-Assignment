import string

def ma_hoa (text, x):
    alphabet = string.ascii_uppercase
    new_alp = alphabet[x:] + alphabet[:x]
    
    x = x % 26
    shift = str.maketrans(alphabet, new_alp)

    result = text.translate(shift)

    print (result)

def giai_ma (text, x):
    alphabet = string.ascii_uppercase
    new_alp = alphabet[( len(alphabet)- x):] + alphabet[:( len(alphabet)-x )]

    x = x%26
    shift = str.maketrans(alphabet, new_alp)

    result = text.translate(shift)

    print (result)

ma_hoa('PYTHON', 13 )
giai_ma('CLGUBA', 13 )
