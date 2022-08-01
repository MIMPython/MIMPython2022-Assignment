def check_password_strength(pass_word):
    if len(pass_word) < 8:
        return False
    
    ascii_letter = []
    for letter in pass_word:
        ascii_letter.append(ord(letter))
        
    sum_capitalized_letter = 0
    for ele in ascii_letter:
        if 65 <= ele and ele <= 90:
            sum_capitalized_letter += 1
            
    sum_normal_letter = 0
    for ele in ascii_letter:
        if 97 <= ele and ele <= 122:
            sum_normal_letter += 1
            
    sum_numeric_letter = 0
    for ele in ascii_letter:
        if 48 <= ele and ele <= 57:
            sum_numeric_letter += 1
            
    sum_special_letter = 0
    for ele in ascii_letter:
        if (33 <= ele and ele <= 47) or (58 <= ele and ele <= 64) or (92 <= ele and ele <= 96) or (123 <= ele and ele <= 126):
            sum_special_letter += 1
            
    multify = sum_special_letter*sum_capitalized_letter*sum_normal_letter*sum_numeric_letter
    if multify == 0:
        return False
    
    return True

user_name = input("Enter your username: ")
user_password = input("Enter your password: ")
while check_password_strength(user_password) == False:
    user_password = input("Your password isn't strong enough, please reenter your password: ") 
    verify_user_password = input("Verify your password : ")
verify_user_password = input("Verify your password : ")
while user_password != verify_user_password:
    print("Verified password is wrong, please reenter your password: ")
    verify_user_password = input("Verify your password : ")
user_infor = {'user_name':user_name, 'user_password':user_password}

choice = input("press 1 to provide more information" +
               "\npress 2 to edit your information")

while choice == 1 or choice == 2:

    if choice == 1: 
        type_information = input("what type of information do you want to add? ")
        detail_information = input("detail of your information: ")
        user_infor[type_information] = detail_information
    else:
        user_name = input("enter your username: ")
        user_password = input("Enter your password: ")
        while check_password_strength(user_password) == False:
            user_password = input("Your password isn't strong enough, please reenter your password: ") 
            verify_user_password = input("Verify your password : ")
        verify_user_password = input("Verify your password : ")
        while user_password != verify_user_password:
            print("Verified password is wrong, please reenter your password: ")
            verify_user_password = input("Verify your password : ")
    
        

#HOW TO HIDE PASSWORD WHEN ENTERING IT ???????



    