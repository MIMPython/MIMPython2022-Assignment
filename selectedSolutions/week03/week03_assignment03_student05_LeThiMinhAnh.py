path = r"E:\MIMPython\week03_student05_LeThiMinhAnh\names.txt"
with open(path, 'r') as f:
    allLines = f.read().split(',')
for x in range(len(allLines)):
    allLines[x] = allLines[x].strip('"')
allLines = sorted(allLines)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nameScoreList = []
for idx, name in enumerate(allLines, 1):
    nameScore = 0
    for character in name:
        nameScore += alphabet.find(character)+1
    nameScore *= idx
    nameScoreList.append(nameScore)
print("Total name score =", sum(nameScoreList))  # Total name score = 871198282
