# change file into a list of names
data = open('week03_assignment03_data.txt', 'r')
names = data.read()[1:-1].split('","')

print(names[0], names[198], names[-1])
# sort the list into alphabetical order
names.sort()

def name2number(name):
    result = []
    for i in range(len(name)):
        result.append(ord(name[i]) - ord('A') + 1)
    return result

print(name2number('ALICE'))


def sum_name_score(names):
    result = 0
    for i in range(len(names)):
        num_ord = i + 1
        score = sum(name2number(names[i])) * num_ord
        result += score
    return result

print(sum_name_score(names)) # 871198282

