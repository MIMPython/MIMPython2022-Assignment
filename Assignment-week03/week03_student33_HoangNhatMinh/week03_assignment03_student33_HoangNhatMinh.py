with open('week03_assignment03_data.txt') as data:
    names = data.readline().strip('"').split('","')

names = sorted(names)
totalNameScore = 0
for order, name in enumerate(names, 1):
    nameScore = 0
    for char in name:
        nameScore = nameScore + ord(char) - 64
    totalNameScore = totalNameScore + nameScore * order

print(totalNameScore)
