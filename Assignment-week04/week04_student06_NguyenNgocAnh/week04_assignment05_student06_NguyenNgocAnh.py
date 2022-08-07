ABC_Morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
}


def morse_to_ABC(string):
    morse_list = string.split(' ')
    morse_list = [ele.strip(' ') for ele in morse_list]
    string_out_ABC = ""
    for element in morse_list:
        string_out_ABC += str(ABC_Morse_dict[element])
    return string_out_ABC


def DOT_DASH_to_morse(string):
    string_ABC_to_morse = string.replace('DOT', '.')
    string_ABC_to_morse = string_ABC_to_morse.replace('DASH', '-')
    string_ABC_to_morse = string_ABC_to_morse.replace('SPACE', ' ')
    return string_ABC_to_morse


def morse_to_real_abc(string):
    string_out = ''
    dot_dash = ''
    for i in range(len(string)):
        if string[i] == '.' or string[i] == '-':
            dot_dash += string[i]
        elif string[i] == ' ':
            string_out += ABC_Morse_dict[dot_dash]
            dot_dash = ''
        else:
            string_out += string[i]
    string_out += ABC_Morse_dict[dot_dash]
    return string_out


if __name__ == '__main__':
    str_morse = '.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- ' \
                '- -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... ' \
                '.... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ' \
                '... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. ' \
                '.- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'

    ABC_string_with_dot_dash = morse_to_ABC(str_morse)
    print(ABC_string_with_dot_dash)
    ABC_and_morse = DOT_DASH_to_morse(ABC_string_with_dot_dash)
    print(ABC_and_morse)
    ABC_real_string = morse_to_real_abc(ABC_and_morse)
    print(ABC_real_string)
