with open("p022_names.txt", "r") as f:
    data = f.read().split(",")

data.sort()
names_scores = []  # a list will contain our numbers scores
name_score = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for index in range(len(data)):  # running through names in our data
    for i in range(len(data[index])):  # running through letters in our name
        for j in range(len(alphabet)):  # running through the alphabet string
            if data[index][i] == alphabet[j]:  # find letters value
                name_score += j
    name_score = name_score * index
    temp = name_score  # using a temp variable to avoid messing up
    names_scores.append(temp)
    name_score = 0  # turn this variable to the initial value for a new name value
print(sum(names_scores))
