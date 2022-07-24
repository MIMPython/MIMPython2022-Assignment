letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def Caesar(Word, RotNumber):
    answer = ""
    for char in Word:
        answer += letters[(letters.index(char.upper()) + RotNumber) % 26]
    return answer

def decoding(Word, RotNumber):
    answer = ""
    for char in Word:
        answer += letters[(letters.index(char.upper()) - RotNumber) % 26]
    return answer

if __name__ == '__main__':
    print(Caesar("PYTHON", 19))   # IRMAHG
    print(Caesar("JAVA", 19))   # CTOT
    print(Caesar("C", 13))   # P