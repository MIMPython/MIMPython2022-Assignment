# bai tap 5 : Ma morse

if __name__ == '__main__':
    code = '.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....\
'
listCharactor = code.split(' ')
morseDictionary = {'.-': 'A',
                   '-...': 'B',
                   '-.-.': 'C',
                   '-..': 'D',
                   '.': 'E',
                   '..-.': 'F',
                   '--.': 'G',
                   '....': 'H',
                   '..': 'I',
                   '.---': 'J',
                   '-.-': 'K',
                   '.-..': 'L',
                   '--': 'M',
                   '-.': 'N',
                   '---': 'O',
                   '.--.': 'P',
                   '--.-': 'Q',
                   '.-.': 'R',
                   '...': 'S',
                   '-': 'T',
                   '..-': 'U',
                   '...-': 'V',
                   '.--': 'W',
                   '-..-': 'X',
                   '-.--': 'Y',
                   '--..': 'Z',
                   }
for element in listCharactor:
    print(morseDictionary.get(element), end='')

# ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH
# may be: All I want to say is dot dot space dot dash ....
