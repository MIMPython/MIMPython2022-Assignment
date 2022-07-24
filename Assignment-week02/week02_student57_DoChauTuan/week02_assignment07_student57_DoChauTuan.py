def encoding(code):
    res = ""
    for i in range(len(code)):
        index = old_code.index(code[i])
        res += new_code[index]
    return res
def decoding(code):
    res = ""
    for i in range(len(code)):
        index = new_code.index(code[i])
        res += old_code[index]
    return res
if __name__ == "__main__":
    old_code = [chr(ascii) for ascii in range(65, 91)]
    new_code = old_code[13:]
    new_code.extend(old_code[:13])
    print(encoding("PYTHON"))
    print(decoding("CLGUBA"))
