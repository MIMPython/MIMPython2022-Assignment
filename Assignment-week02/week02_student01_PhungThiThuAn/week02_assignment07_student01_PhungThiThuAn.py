# hàm tạo ra mật mã Ceaser:
def create_caeser_code(word):
    word = word.upper()
    char_array = list(word)
    result = ''
    for i in char_array:
        if 'A' <= i < chr(ord('A') + 13):
            result += chr(ord(i)+13)
        if chr(ord('A') + 13) <= i <= 'Z':
            result += chr(ord(i)-13)
    return result

print(create_caeser_code('Python'))  # CLGUBA

# hàm giải mật mã Caeser:
def solve_caeser_code(word):
    word = word.upper()
    char_array = list(word)
    result = ''
    for i in char_array:
        if 'A' <= i < chr(ord('A') + 13):
            result += chr(ord(i)+13)
        else:
            result += chr(ord(i)-13)
    return result

print(solve_caeser_code('clguba'))  # PYTHON


