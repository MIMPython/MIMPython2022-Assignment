import argparse
import re
import string
import sys


#Chuyển đổi tên về đúng dạng theo quy định
def convertName(name):
    # Chuyển tiếng việt có dấu thành không dấu
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

    nameList = output.title()
    return "".join(nameList.split())

    # Chuyển đổi số về đúng dạng
def convertNum(number):
    # Nếu người dùng cố tình nhập số âm
    if (number < 0):
        return -number

    # Nếu số là 1 số nhỏ hơn 10
    elif number < 10:
        return "0"+str(number)
    return number

    # Theo đúng yêu cầu của đề bài không yêu cầu nhập ID
def assignment(name, week, exercise):
    # Chuyển đổi các dữ liệu về đúng với dạng theo yêu cầu
    name = convertName(name)
    week = convertNum(week)
    exercise = convertNum(exercise)
    return "week{}_assignment{}_{}.py".format(week,exercise,name)

    # Theo đúng quy định về định dạng file bài tập của khóa học
def assignmentWithID(name, week, exercise,id = 0):
    name = convertName(name)
    week = convertNum(week)
    exercise = convertNum(exercise)
    id = convertNum(id)
    return "week{}_assignment{}_student{}_{}.py".format(week,exercise,id,name)


if __name__ == '__main__':


    infor = sys.argv
    infor.pop(0)
    print(infor)

    name,week,exercise,id = str(infor[0]) , int(infor[1]),int(infor[2]),int(infor[3])

    print("______________________\n")
    print("Your file name is: "+ assignment(name ,week,exercise))
    print("______________________\n")
    print("Your full file name is: "+ assignmentWithID(name, week, exercise,id))
