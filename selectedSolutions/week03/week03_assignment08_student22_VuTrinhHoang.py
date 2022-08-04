import maskpass
def check(Password):
    count = 0
    if len(Password)>=12:
        count += 1
    for i in Password:
        if (ord(i)>=33&ord(i)<=47)|(ord(i)>=58&ord(i)<=64)|(ord(i)>=123&ord(i)<=126):
            count += 1
        elif ord(i)>=48&ord(i)<=57:
            count += 1
        elif ord(i)>=65&ord(i)<=90 :
            count += 1
        elif ord(i)>=97&ord(i)<=122 :
            count += 1
    if Password.find("123") == -1:
        count += 1
    if Password.find("abc") == -1:
        count += 1
    if Password.find("ABC") == -1:
        count += 1
    if Password != Username:
        count += 1
    if count >= 15:
        return "strong"
    elif count>=10& count<15:
        return "normal"
    else :
        return "weak"
    
print("input your username:")
Username=input()

print("input your password:")
print("*note: password require special characters, number, normal and Capitalization alphabet:")
Password= maskpass.askpass() 

while check(Password)=="normal":
    print("Your password are not really strong, do you wanna to change? y for yes and n for no !")
    print("*note: password require special characters, number, normal and Capitalization alphabet:")
    n=input()
    if n=="y":
        print("input your password:")
        Password= maskpass.askpass() 
    else :
        break
    
while check(Password)=="weak":
    print("your password are too weak, please use another!")
    print("input your password:")
    Password= maskpass.askpass() 

print(check(Password))
print("please confirm your password:")
RePassword= maskpass.askpass() 
while RePassword != Password:
    print("your password are not match, please re-input")
    RePassword= maskpass.askpass() 