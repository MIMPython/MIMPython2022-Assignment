def rot13Encode(code):
    code = str(code).upper()
    rot13Code = ""
    for i in code:
        charNum = ord(i)
        if charNum>=78:
            charNum-=13
        else:
            charNum+=13
        rot13Code+=chr(charNum)
    return rot13Code

def rot13Decode(code):
    code = str(code).upper()
    rot13Code = ""
    for i in code:
        charNum = ord(i)
        if charNum<=77:
            charNum+=13
        else:
            charNum-=13
        rot13Code+=chr(charNum)
    return rot13Code

if __name__ == '__main__':
    choice = int(input("Input 1 to Encode and 2 to Decode: "))
    while choice!=1 and choice !=2:
        print("Plese only input 1 or 2!")
        choice = int(input("Input 1 to Encode and 2 to Decode: "))
    if choice == 1:
        code = str(input("Input string of code you want to Encode: "))
        print(rot13Decode(code))
    else:
        code = str(input("Input string of code you want to Encode: "))
        print(rot13Decode(code))
    

