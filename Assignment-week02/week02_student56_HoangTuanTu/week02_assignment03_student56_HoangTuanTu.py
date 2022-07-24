import re

def convertName(name):

    patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y' }

    output = name
    for regex, replace in patterns.items():
        output = re.sub(regex.upper(), replace.upper(), output)

    nameList = output.split()

    for i in range(len(nameList)):
       nameList[i]=nameList[i].capitalize()

    output = "".join(nameList)
    return output

def convertNum(number):
    if (number < 0):
        return -number
    elif number < 10:
        return "0"+str(number)
    return number

def assignment(name, week, exercise):
    name = convertName(name)
    name = "".join(name.split())
    week = convertNum(week)
    exercise = convertNum(exercise)
    return "week{}_assignment{}_{}.py".format(week,exercise,name)

def assignmentWithID(name, week, exercise,id):
    name = convertName(name)
    name = "".join(name.split())
    week = convertNum(week)
    exercise = convertNum(exercise)
    id = convertNum(id)
    return "week{}_assignment{}_student{}_{}.py".format(week,exercise,id,name)


if __name__ == '__main__':
    name = str(input("Input name: "))
    week = int(input("Input week of assignment: "))
    exercise = int(input("Input number of exercise: "))
    id = int(input("Input your ID: "))

    print("______________________\n")
    print("Your file name is: "+ assignment(name ,week,exercise))
    print("______________________\n")
    print("Your full file name is: "+ assignmentWithID(name, week, exercise,id))
