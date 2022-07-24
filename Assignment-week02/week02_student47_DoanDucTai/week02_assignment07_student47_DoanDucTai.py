import code


def codingChar(x):
    if ("a" <= x <= "m"):
        return chr(ord(x) + 13)
    elif ("n" <= x <= "z"): 
        return chr(ord(x) - 13)
    if ("A" <= x <= "M"):
        return chr(ord(x) + 13)
    elif ("N" <= x <= "Z"): return chr(ord(x) - 13)
def decodeChar(x):
    if ("n" <= x <= "z"):
        return chr(ord(x) - 13)
    elif ("a" <= x <= "m"):
        return chr(ord(x) + 13)
    if ("A" <= x <= "M"):
        return chr(ord(x) + 13)
    elif ("N" <= x <= "Z"): return chr(ord(x) - 13)
code = input("nhập mã: ")
def coding(x):
    st = ""
    for i in x :
        st = st + codingChar(i)
    return st
def decode(x):
    st = ""
    for i in x :
        st = st + decodeChar(i)
    return st
print("mã hóa: ", coding(code))
print("giải mã: ", decode(code))