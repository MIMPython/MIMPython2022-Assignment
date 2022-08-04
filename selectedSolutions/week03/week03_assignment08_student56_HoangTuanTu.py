import os
"""
Chương Trình này hiện chưa hoàn thiện do nhiều vấn đề chủ quan
"""
def accesByUserName(data):
    if len(data)<=2:
        return dict()
    acccess = dict()
    for i in range(0,len(data),2):
        acccess.setdefault(data[i],data[i+1])
    return acccess

listData = list()
with open("data.txt",'r+',encoding = 'utf-8') as file:
    listData = str(file.read()).split("\n")
access = accesByUserName(listData)


def nonDigitInPass(password):
    digit = [1,2,3,4,5,6,7,8,9,0]
    for i in digit:
        if str(i) in password:
            return False
    return True

def nonUpperLetterInPass(password):
    for i in password:
        if ord(i)>=65 and ord(i)<=90:
            return False
    return True    

def nonLowerLetterInPass(password):
    for i in password:
        if ord(i)>=97 and ord(i)<=122:
            return False
    return True   

def nonSpecial(password):

    char = [chr(i) for i in range(97,122)]
    char.extend([chr(i) for i in range(65,90)])
    char.extend([chr(i) for i in range(48,57)])

    for i in password:
        if str(i) not in char:
            return False
    return True   

def checkingPassWord(password):
    if len(password)<8:
        return False
    elif nonDigitInPass(password):
        return False
    elif nonUpperLetterInPass(password):
        return False
    elif nonLowerLetterInPass(password):
        return False
    elif nonSpecial(password):
        return False
    return True

def userInput():
    with open("data.txt",'r',encoding = 'utf-8') as file:
        userName = str(input("Input your username: "))

        while userName not in listData:
            print("Unavailable user name! Please retype")
            userName = str(input("Input your username: "))
        
        password = str(input("Input pass word: "))
        while access[userName] != password :
            print("Wrong password!")
            password = str(input("Input pass word: "))
        print("Access Successful!")

def tutorial():
    os.system("cls")
    print("""
Input your choice to use our Service!
""")

def feature():
    print("""
Choise 0 to exit()
Choise 1 to create account
Choise 2 to login
""")
    choise = int(input("Your choise: "))
    while choise<0 or choise >2:
        print("Only input 1 or 2 or 0 to exit: ")
        choise = int(input("Your choise: "))
    return choise

def createAccount():
    userName = str(input("Input username: "))
    while userName in listData:
        print("Username have been use!")
        userName = str(input("Input username: "))

    password = str(input("Input password: "))
    while checkingPassWord(password)==False:
        print("Your password is unsafe enough!")
        password = str(input("Input password: "))
    access.setdefault(userName,password)
    print("Complete!")
def toFile():
    file = open("data.txt",mode="w+")
    toFileData = ""
    print(access)
    for key in access.keys():
        toFileData+= "\n"+ str(key)+"\n"+access[key]
    file.write(toFileData)
    file.close()


if __name__ == "__main__":
    tutorial()
    choice = int(feature())
    if choice == 2:
        userInput()
    elif choice == 1:
        createAccount()
        toFile()
    print("Thank for using our service!")
