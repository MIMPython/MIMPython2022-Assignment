letterUpperbound = ord('z')
letterLowerbound = ord('a')
digitUpperbound = ord('9')
digitLowerbound = ord('0')

# [chr(x) for x in range(letterLowerbound, letterUpperbound+1)]
charLst = [chr(x) for x in range(letterLowerbound, letterUpperbound+1)] + [chr(i) for i in range(digitLowerbound, digitUpperbound+1)]
print(charLst)

codeLst = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

def solveMorsecode(code):
    splitedCode = code.split(' ')
    output = ''
    for i in range(0, len(splitedCode)):
        for j in range(0, len(codeLst)):
            if codeLst[j] == splitedCode[i]:
                output += charLst[j]
                break
    return output

print(solveMorsecode('.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'))

''' alliwanttosayisdotdotspacedotdashdotdotspacedashdashdashspacedotdotdotdashspacedotspacedashdotdashdashspacedashdashdashspacedotdotdash

'''

print(solveMorsecode('.. .-.. --- ...- . -.-- --- ..-'))
''' 
iloveyou
'''