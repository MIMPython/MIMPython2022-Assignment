# Bài tâp 8: banking simulation
from getpass4 import getpass


def register():
    userName = input("Enter User name ")
    password = getpass("Enter Password ")
    while isSecurePass(password) != True:
        print("Password length have to  least 8 charactor, contain both upper and lower, number, ")
        password = getpass("Password is not secure, please try again")

    confirmPass = getpass("Confirm password ")
    while confirmPass != password:
        confirmPass = getpass(
            "confirm password is difference with password, please try again")
    # Person information
    # fullName = input("Your Fullname ")
    # age = int(input("Age "))
    # address = input("Address ")
    # phoneNumber = input("Number")

    print("Register successfully")
    # fullName: {fullName}; age: {age}; address: {address}; phoneNumber: {phoneNumber}
    user = f"UserName: {userName};password: {password};\n"
    with open('user.txt', 'a') as f:
        f.write(user)
        f.close()


def isSecurePass(password):

    if len(password) < 8:
        return False
    if password.islower() or password.isupper():
        return False
    if password.isnumeric():
        return False
    # more required
    return True


if __name__ == "__main__":
    register()
