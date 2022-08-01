path = 'D:\Downloads\\names.txt'
with open(path, 'r') as f:
    allNames = f.read()[1:-1].split('","')

# Sorting it into alphabetical order
allNames.sort()
 
# Working out the alphabetical value for each name
def valueForName(name):
    value = 0
    for i in range(len(name)):
        temp = ord(name[i]) - ord('A') + 1
        value = value + temp
    return value

# The total of all the name scores in the file
def calSum(names):
    sum = 0
    for i in range(len(names)):
        n = i + 1 # Its alphabetical position in the list 
        score = valueForName(allNames[i]) * n
        sum = sum + score
    return sum

print(calSum(allNames)) # 871198282