
file_path = 'D:\person_names.txt'
with open(file_path, 'r') as file_object:
    lines = sorted(file_object.read()[1:].split('","'))

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = range(1, 27)
count_alphabets = dict(zip(alphabets, numbers))

def name_scores(name):
        if name not in lines:
            print("")
        sum = 0
        for i in name.upper():
            sum += count_alphabets[i]    
        scores = lines.index(name.upper()) * sum
        print(scores)
name_scores('GERALDINE') #134100
name_scores('GLADYS')    #124576
name_scores('TINA')      #209880