def morseCodeTrans(morse=""):
    morseList = morse.split(" ")
    with open("additionalFolder\\morseCode.txt",'r+',encoding = 'utf-8') as file:
        morseCode = str(file.read()).replace(" ","").split("\n")
    for i in range(len(morseList)):
        for j in range(len(morseCode)):
            if morseList[i]==morseCode[j]:    
                morseList[i] = str(chr(j+65))
    morse =" ".join(morseList)
    return morse
    
def toMorse(code):
    code = str(code).replace(" ","")
    morse = {"DOT":".","DASH":"-","SPACE":" "}
    for i in morse.keys():
        if i in code:
            code = code.replace(i,morse[i])

    onlyMorse = ""
    noMorse = ""

    for i in range(len(code)):
        if code[i] in morse.values():
            onlyMorse+=code[i]
        else:
            noMorse+=code[i]

    onlyMorse = morseCodeTrans(onlyMorse)
    last = noMorse+" "+onlyMorse
    return last

if __name__ == "__main__":
    moreseCode = str(input("Input morse code: "))
    moreseTrans = morseCodeTrans(moreseCode)
    print("After translating is:","".join(moreseTrans.split()))
    print("This still have something hide in it!")
    print("The last word is: "+toMorse(moreseTrans))
    #ALL I WANT TO SAY IS I LOVE YOU
