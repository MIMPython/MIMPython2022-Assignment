# Bài tập 7: Mã hóa vào giải mã theo mã ROT-13
# Mã Caesar Rot-13 được mô tả như là: ký tự x sẽ được mã hóa bằng ký tự phía trước x 13 ký tự theo bảng chữ cái, và tất cả các chữ cái đều được mã hóa như thế. Dãy chữ cái đươc cấu trúc theo dạng vòng.

# Hàm lấy giá trị của charactor
def getValueCharactor(x):
    return ord(x)

# Hàm mã hóa
# các chữ cái từ A đến Z (viết hoa) trong bảng mã ASCII có giá trị từ 65 đến 90
# hàm encodeCharactor thực hiện mã hóa 1 ký tự thuộc bảng chữ cái theo quy tắc lấy giá trị biểu diễn của chữ cái đó + 13. Nếu giá trị đó vượt 90 (chữ Z), tức là 91,  thì quay về chữ A có giá trị 65 = 91 - 26, nên nếu giá trị của chữ cái x + 13 lớn hơn 90 thì chữ cái mã hóa của x sẽ có giá trị (x + 13) - 26.


def encodeCharactor(x):
    if ord(x) < 65 or ord(x) > 90:
        print("không thuộc miền mã hóa")
        return

    encodeX = ord(x) + 13
    if(encodeX > 90):
        return chr(encodeX - 26)
    return chr(encodeX)

# hàm mã hóa string


def encodeString(str):
    result = ''
    for i in str:
        result = result + encodeCharactor(i)
    return result

# hàm giải mã từng ký tự


def decodeCharactor(x):
    if ord(x) < 65 or ord(x) > 90:
        print("không thuộc miền mã hóa")
        return
    decodeX = ord(x) - 13
    if decodeX < 65:
        return chr(decodeX + 26)
    else:
        return chr(decodeX)


# hàm giải mã xâu
def decodeString(str):
    result = ''
    for i in str:
        result = result + decodeCharactor(i)
    return result


if __name__ == '__main__':
    print(encodeString('ABC'))  # NOP
    print(decodeString('NOP'))  # ABC

    print(encodeString('PYTHON'))  # CLGUBA
    print(decodeString('CLGUBA'))  # PYTHON
