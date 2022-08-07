# nên cho đoạn mã morse vào một file text trước khi tiến hành giải mã để thuận tiện hơn

Dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}


# reading morse code file
file = open('morsecode.txt')
morse_code_in_string = file.readline()
file.close()


def decryption(message):
    message = message.split(" ")
    result = []
    for characters in message:
        if characters in Dict:
            result.append(Dict[characters])
    return "".join(result)


print(decryption(morse_code_in_string))

