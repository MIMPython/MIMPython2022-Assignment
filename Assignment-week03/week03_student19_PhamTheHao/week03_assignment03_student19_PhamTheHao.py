"""
Bài tập 3. (names scores)
Using names.txt, a 46K text file containing over five-thousand first names, begin by 
sorting it into alphabetical order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position in the list to obtain a name 
score. What is the total of all the name scores in the file?

"""

def total_of_name_score():
    total = sum((ord(char) - ord('A') + 1) * i
        for (i, name) in enumerate (names, 1)
        for char in name)
    return total

data = 'names.txt'

with open(data, 'r') as file:
    names = sorted(file.read()[1:-1].split('","'))

print(total_of_name_score())




