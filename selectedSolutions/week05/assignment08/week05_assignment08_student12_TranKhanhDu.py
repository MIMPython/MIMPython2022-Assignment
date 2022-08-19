from encodings import utf_8


filePath = "D:\\VisualCode\\Python\\MIM2022Python\\vietkey.txt"
with open(filePath, encoding='utf_8') as fileObject:
    reader = fileObject.readlines()
    
#create dictionary vie to eng
dictionaryVieToEng = {}
for ele in reader:
    A = ele.split(":")
    dictionaryVieToEng[A[0]] = A[1].strip("\n")


#create dictionary eng to vie
dictionaryEngToVie = {}
for ele in reader:
    A = ele.split(":")
    dictionaryEngToVie[A[1].strip("\n")] = A[0]
print(dictionaryEngToVie)

def convertVieToEng(string1):
    string1.lower()
    convertedString = ""
    for letter in string1:
        if ord(letter) < 97 or ord(letter) > 122:
            letter = dictionaryVieToEng[letter]
            convertedString += letter
        else: 
            convertedString += letter
    print(convertedString)
a = input()
convertVieToEng(a)

def convertEngToVie(string2):
    string2.lower()
    convertedString = ""
    for letter in range(0, len(string2) - 3):
        for element in dictionaryVieToEng:
            if string2[letter] + string2[letter + 1] == dictionaryVieToEng[element]:
                convertedString += dictionaryEngToVie[element]
                continue
            elif string2[letter] + string2[letter + 1] + string2[letter + 2] == dictionaryVieToEng[element]:
                convertedString += dictionaryEngToVie[element]
                continue
                continue
            else: 
                convertedString += string2[letter]
    print(convertedString)
    
a = input()
convertEngToVie(a)