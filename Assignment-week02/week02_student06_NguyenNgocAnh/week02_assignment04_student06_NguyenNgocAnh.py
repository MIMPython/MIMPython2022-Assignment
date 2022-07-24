# kiem tra tu có xuat hien trong doan van hay khong
# neu co thi tra ve True, khong tra ve False
def check_word(word, words):
    print(word.lower() in words)
    # lower() dung de kiem tra vi da dua ve dang viet thuong


# dem tan suat xuat hien cua mot tu
def count_word(word, words):
    cnt = 0
    for i in range(len(words)):
        if word.lower() == words[i]:
            cnt += 1
    print("'" + word + "'" + ' xuat hien ' + str(cnt) + ' lan.')


# dem so tu trong doan
def count_number_of_word(words):
    print('So tu: ' + str(len(words)))


# in hoa cau dau tien trong doan
def upper(string):
    strs = string.split('. ')
    strs[0] = strs[0].upper()
    new_str = ''
    for i in range(len(strs)):
        if i == len(strs) - 1:
            new_str += strs[i]
        else:
            new_str += strs[i] + '. '
    print(new_str)


if __name__ == '__main__':
    string_example = 'Python was designed to be easy to understand ' \
                     'and fun to use (its name came from Monty Python' \
                     ' so a lot of its beginner tutorials reference it).' \
                     ' Fun is a great motivator, and since you’ll be able' \
                     ' to build prototypes and tools quickly with Python,' \
                     ' many find coding in Python a satisfying experience.' \
                     ' Thus, Python has gained popularity for being a' \
                     ' beginner-friendly language, and it has replaced' \
                     ' Java as the most popular introductory language at' \
                     ' Top U.S. Universities.'
    # clean
    # chuyen ve lower
    words_of_string = string_example.lower()
    # chia nho tu
    words_of_string = words_of_string.split()
    # xoa ki tu dac biet
    words_of_string = [word_in_words.strip('.,!;(){}[]')
                       for word_in_words in words_of_string]
    words_of_string = [word_in_words.replace("'s", '')
                       for word_in_words in words_of_string]

    # kiem tra Python, contains, experience, difficult
    check_word('Python', words_of_string)
    check_word('contains', words_of_string)
    check_word('experience', words_of_string)
    check_word('difficult', words_of_string)

    # dem so tu xuat hien
    count_word('Python', words_of_string)

    # dem tu trong doan van
    count_number_of_word(words_of_string)

    # in hoa
    upper(string_example)
