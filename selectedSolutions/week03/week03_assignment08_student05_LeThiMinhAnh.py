import re
import maskpass


def banking_simulation():
    userName = input("Enter your username: ")
    print("""
    The password must contain:
    - At least 8 characters
    - At least 1 lowercase character
    - At least 1 uppercase character
    - At least 1 number 
    - At least 1 special character (@,$,!,%,*,?,&)
    """)
    isOK = False
    while not isOK:
        passWord = maskpass.askpass(prompt="Enter your password: ", mask="*")
        isOK = checkPasswords(passWord)
        if isOK:
            print("Password is OK.")
    confirmCondition = False
    while not confirmCondition:
        confirmPwd = maskpass.askpass(
            prompt="Confirm your password: ", mask="*")
        confirmCondition = confirmPasswords(confirmPwd, passWord)


def checkPasswords(pwd):
    condition = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    match = re.search(condition, pwd)
    if match:
        return True
    elif len(pwd) < 8:
        print("Password is too short, please try again")
        return False
    elif not re.findall("\d", pwd):
        print("Password must contain at least 1 number, please try again")
        return False
    elif not re.findall("[a-z]", pwd):
        print("Password must contain at least 1 lowercase character, please try again")
        return False
    elif not re.findall("[A-Z]", pwd):
        print("Password must contain at least 1 uppercase character, please try again")
        return False
    else:
        print("Password must contain at least 1 special character (@,$,!,%,*,?,&), please try again")
        return False


def confirmPasswords(confirmPwd, pwd):
    if confirmPwd == pwd:
        print("Password match!")
        return True
    else:
        print("Password did not match, please try again.")
        return False


banking_simulation()
