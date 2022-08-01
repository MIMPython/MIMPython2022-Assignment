#bài 5. Kéo - Búa - Bao

import os


#a
person1 = input("lựa chọn của người 1: ").lower().strip()
person2 = input("lựa chọn của người 2: ").lower().strip()
def personWin (n1, n2):
    if (n1 == n2):
        print("Hòa")
    elif ( n1 == "kéo" and n2 == "búa"):
        print("Người thứ 2 thắng.")
    elif ( n1 == "bao" and n2 == "kéo"):
        print("Người thứ 2 thắng.")
    elif ( n1 == "búa" and n2 == "bao"):
        print("Người thứ 2 thắng.")
    elif ( n2 == "kéo" and n1 == "búa"):
        print("Người thứ 1 thắng.")
    elif ( n2 == "bao" and n1 == "kéo"):
        print("Người thứ 1 thắng.")
    else:
        print("Người thứ 1 thắng.")
personWin(person1, person2)
#person1 = búa
#person2 = bao
#personWin(person1, person2)  # Người thứ 2 thắng.

#b
person_1 = input("lựa chọn của người 1: ").lower()
os.system('CLS')    #xóa màn hình
person_2 = input("lựa chọn của người 2: ").lower()
os.system('CLS')    #xóa màn hình 
personWin(person_1, person_2)

