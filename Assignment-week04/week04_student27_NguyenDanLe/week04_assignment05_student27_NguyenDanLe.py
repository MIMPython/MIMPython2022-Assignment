"""Khi nhận được đoạn mã Morse, ta phải tạo một phần mềm để có thể dịch mã Morse.
    Giữa các chữ cái của một từ phân biệt với nhau bởi một dấu cách.
    Giữa các từ phân biệt với nhau bởi hai dấu cách."""
from email import message


morse_code = { '.-': 'A', '-...': 'B',
                    '-.-.': 'C', '-..': 'D', '.': 'E',
                    '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K',
                    '.-..': 'L','--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P', '--.-': 'Q',
                    '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W',
                    '-..-': 'X', '-.--': 'Y', '--..':'Z',
}
message = ".- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."
split = message.split()
decode_message = ""
for i in split:
    decode_message += morse_code[i]
print(decode_message)