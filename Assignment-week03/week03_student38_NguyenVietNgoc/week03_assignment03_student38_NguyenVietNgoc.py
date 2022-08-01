def score(name, pos):
    score = 0

    for letter in name:
        if letter == "A": score += 1
        elif letter == "B": score += 2
        elif letter == "C": score += 3
        elif letter == "D": score += 4
        elif letter == "E": score += 5
        elif letter == "F": score += 6
        elif letter == "G": score += 7
        elif letter == "H": score += 8
        elif letter == "I": score += 9
        elif letter == "J": score += 10
        elif letter == "K": score += 11
        elif letter == "L": score += 12
        elif letter == "M": score += 13
        elif letter == "N": score += 14
        elif letter == "O": score += 15
        elif letter == "P": score += 16
        elif letter == "Q": score += 17
        elif letter == "R": score += 18
        elif letter == "S": score += 19
        elif letter == "T": score += 20
        elif letter == "U": score += 21
        elif letter == "V": score += 22
        elif letter == "W": score += 23
        elif letter == "X": score += 24
        elif letter == "Y": score += 25
        elif letter == "Z": score += 26
        else: score += 0
    return score * pos

with open('names.txt', 'r') as nameList:
    data = nameList.read().split(",")
    data = [str(name) for name in data]
    data.sort()

totalScore = 0
pos = 1

for name in data:
    totalScore += score(name, pos)
    pos += 1 

print (totalScore)  # 871198282