from random import randint

print("Nhap Keo, Bua, Bao")

player = input()

computer = randint(0,2)


if computer == 0:
   computer = "Bua"

if computer == 1:

   computer = "Bao"

if computer == 2:

   computer = "Keo"

print("-----")

print("Ban chon: " + player)

print("May chon: " + computer)

print("-----")


if computer == player: 

 print("Hoa")

else:
   if player == "Bao":

      if computer == "Bua":

         print("Ban Thang")

      else:

         print("Ban Thua")


   elif player == "Bua":

      if computer == "Keo":

         print("Ban Thang")

      else:

         print("Ban Thua")


   elif player == "Keo":

      if computer == "Bao":

         print("Ban Thang")

      else:

         print("Ban Thua")
   
   else:

     print("Nhap sai roi!")