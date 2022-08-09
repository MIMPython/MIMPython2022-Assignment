morseCodeAlphabet = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
                     "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2",    "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}
with open("morsecode.txt", "r") as f:
    morseCode = f.readlines()[0]


def morse_to_text(morseCode):
    message = morseCode.split(" ")
    text = ""
    for i in message:
        if i in morseCodeAlphabet:
            text += morseCodeAlphabet[i]
    return text


firstText = morse_to_text(morseCode)
print(firstText)  # ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH
# Ta thấy đoạn mã code sau khi giải thì vẫn chứa một đoạn mã morse nhưng dưới dạng chữ
morseText = firstText[min(firstText.find("DASH"), firstText.find("DOT")):]


def morse_text_to_morse(morseTxt):
    replaceDict = {"DASH": "-", "DOT": ".", "SPACE": " "}
    for i in replaceDict:
        morseTxt = morseTxt.replace(i, replaceDict[i])
    return morseTxt


finalText = firstText[:min(firstText.find("DASH"), firstText.find("DOT"))] + \
    morse_to_text(morse_text_to_morse(morseText))
print(finalText)  # ALLIWANTTOSAYISILOVEYOU

# Nên làm gì khi nhận được đoạn mã Morse trên:
print(morse_to_text(
    ".. -- ... --- .-. .-. -.-- -... ..- - .-- . .-. . .--- ..- ... - ..-. .-. .. . -. -.. ..."))  # IMSORRYBUTWEREJUSTFRIENDS
