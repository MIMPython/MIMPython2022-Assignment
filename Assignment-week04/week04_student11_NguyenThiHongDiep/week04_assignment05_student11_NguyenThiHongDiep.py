# Từ điển của mã Morse
MorseCodeDict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def Decrypt(text): # Hàm giải mã
    CipherText = '' # Khai báo văn bản mật mã là một văn bản rỗng
    PlainText = '' # Khai báo văn bản thô là một văn bản rỗng
    for i in (text + ' '):
        if (i != ' '):
            CipherText += i
        else:
            PlainText += list(MorseCodeDict.keys())[list(MorseCodeDict.values()).index(CipherText)]
            CipherText = ''
    return PlainText

print(Decrypt('.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'))
# ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH

print(Decrypt('.. .-.. --- ...- . -.-- --- ..-'))
# ILOVEYOU

# I will say '.. .-.. --- ...- . -.-- --- ..- - --- ---'
print(Decrypt('.. .-.. --- ...- . -.-- --- ..- - --- ---'))
# ILOVEYOUTOO


