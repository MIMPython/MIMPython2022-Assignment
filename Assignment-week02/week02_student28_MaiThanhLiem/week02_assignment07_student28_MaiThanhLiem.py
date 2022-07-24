lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot_13(word):
    new_word = ""
    for i in range(len(word)):
        if (word[i] in lower_alphabet) == True:
            for index1 in range(len(lower_alphabet)):
                if word[i] == lower_alphabet[index1]:
                    new_index = (index1 + 13) % 26
                    new_word += lower_alphabet[new_index]
        elif (word[i] in upper_alphabet) == True:
            for index2 in range(len(upper_alphabet)):
                if word[i] == upper_alphabet[index2]:
                    new_index = (index2 + 13) % 26
                    new_word += upper_alphabet[new_index]
        else:
            new_word += word[i]
    print(new_word)


rot_13("Python 3.10.5 ")
rot_13("Unir n jbaqreshy 7/26.")
