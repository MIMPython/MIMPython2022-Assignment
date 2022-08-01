char_to_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
                 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# reading file
file = open('names.txt')
list_in_string = file.readline()
file.close()
names_list = sorted(str(list_in_string).split(','))


# building function calculate name's score
def name_score(name, index):
    score = 0
    for char in name:
        score += char_to_score[char]
    return score * index


# final score
final_score = 0
index = 1
for name in names_list:
    final_score += name_score(name, index)
    index += 1

print(final_score)  # 871198282
